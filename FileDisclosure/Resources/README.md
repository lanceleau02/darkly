# 📁 File Disclosure

## 📖 Definition

A **File Disclosure** breach occurs when an attacker gains unauthorized access to the `.htpasswd` file, which is typically used to store hashed passwords for basic HTTP authentication. The `.htpasswd` file is intended to be protected by the web server configuration, but if improperly secured, it can be accessed directly or through exploitation of vulnerabilities.

This breach is often associated with:

1. **Server Misconfigurations:** When the web server does not restrict access to sensitive files.

2. **Path Traversal Vulnerabilities:** When attackers manipulate file paths to bypass security controls and access `.htpasswd`.

3. **Weak Permissions:** When file permissions allow unauthorized users to read the `.htpasswd` file.

4. **Information Disclosure Vulnerabilities:** If the file is exposed due to directory listing or insufficient security measures.

If an attacker successfully retrieves the `.htpasswd` file, they can attempt to crack the stored password hashes using brute force or dictionary attacks, potentially compromising the associated user accounts or gaining unauthorized access to protected resources.

## 🔍 Discovery

Thanks to the `robots.txt` file, we navigate to the `http://<ip>/whatever` address and discover the existence of a `htpasswd` file containing: 

```Text
root:437394baff5aa33daa618be47b75cb49
```

This is a `username:password` combination and the password seems to be encrypted, so we can detect the encryption thanks to [dCode](https://www.dcode.fr/cipher-identifier) cipher identifier, this one is in MD5. Once decrypted, we get `qwerty123@` so our final combination is `root:qwerty123@`. Finally, we can go to `http://<ip>/admin/` and enter our credentials.

## 🏁 Flag

1. Go on `http://<ip>/whatever/`
2. Download the `htpasswd` file
3. Decrypt the password using the MD5 algorithm
4. Go on `http://<ip>/admin/`
5. Type `root` as username and `qwerty123@` as password

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Proper Server Configuration:** configure the web server to explicitly deny access to `.htpasswd` files.
- **File permissions:** ensure the file is owned by the web server user (e.g., `www-data`).
- **Strong Authentication Mechanisms:** use modern authentication methods (e.g., OAuth, JWT) instead of `.htpasswd` for sensitive applications.
- **Restrictive Access:** add a `.htaccess` file to restrict access or change the reverse proxy configuration to prevent access to files of this type.

## 🧰 Toolbox

- [dCode Cipher Identifier](https://www.dcode.fr/cipher-identifier)
- [dCode MD5 Decrypter](https://www.dcode.fr/md5-hash)

## 📚 References

- [htpasswd - Manage user files for basic authentication](https://httpd.apache.org/docs/2.4/programs/htpasswd.html)