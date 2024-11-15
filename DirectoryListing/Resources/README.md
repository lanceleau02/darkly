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

**1. The dumb way:**

1. Go on `http://<ip>/.hidden`
2. Browse ALL the directories and download ALL the `README` files you'll find
3. ...

**2. Using a crawler Bash script**

**3. Using a Python script with Scrapy**

**4. Using a Python script with Beautiful Soup**

## 💡 Solutions



