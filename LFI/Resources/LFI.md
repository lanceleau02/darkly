# 🗂️ Local File Inclusion

## 📖 Definition

A **Local File Inclusion (LFI)** breach is a web vulnerability that allows an attacker to exploit a server’s ability to include files by manipulating input parameters to access unauthorized local files stored on the server. This attack typically involves tricking the application into loading files such as configuration files, log files, or sensitive system files.

**Key Characteristics of a Local File Inclusion Breach:**

1. **Exploitation of Input Validation:** LFI attacks occur when user-supplied input is used to construct file paths without proper validation, allowing attackers to insert malicious file paths.

2. **File Access via Path Traversal:** By including directory traversal sequences (e.g., ../../), attackers can navigate the server's file structure and access sensitive files outside the intended scope of the application.

3. **File Inclusion:** The targeted files are often loaded and executed or displayed by the application, potentially revealing sensitive information or leading to further exploitation.

4. **Potential Consequences:**

    - Disclosure of sensitive data (e.g., `passwd`, configuration files).
    - Access to log files that can assist in escalating attacks.
    - Execution of malicious payloads, particularly if combined with upload vulnerabilities (turning LFI into Remote Code Execution, or RCE).

## 🔍 Discovery

By doing some reseaches, we read that a type of breach consists in accessing files (particularly the `etc/passwd` file) by concanate successions of `../` behind the website URL. So we dumbly try to concanate some and we finally get a result at this address:

```URL
http://<ip>/index.php?page=../../../../../../../etc/passwd
```

1. Go on http://192.168.1.16/index.php?page=../../../../../../../etc/passwd

https://book.hacktricks.xyz/pentesting-web/file-inclusion