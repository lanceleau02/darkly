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

## 🏁 Flag

1. Go on `http://<ip>/index.php?page=../../../../../../../etc/passwd`

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

1. **Validate and Sanitize User Input**
    - **Whitelisting File Paths:** Only allow specific, predefined file names or paths to be included, rejecting any input that doesn’t match these safe options. For example, you can restrict file inclusions to a fixed list of allowed files.
    - **Filter Directory Traversal Sequences:** Ensure user inputs cannot include sequences like `../../` that would allow an attacker to navigate outside the intended directories. Implement strict checks on file paths and sanitize inputs to remove or escape dangerous characters.
    - Escape Special Characters: Properly escape or sanitize any special characters (like `../`, `..`, etc.) in user inputs that could manipulate the file path.
2. **Use Full Paths Instead of User-Controlled Input**
    - **Avoid User-Controlled File Paths:** Avoid allowing users to input file paths directly. Instead, specify paths using predefined constants or configuration settings, ensuring the application never constructs paths dynamically from user input.
    - **Restrict File Access to a Specific Directory:** Ensure that files are only loaded from specific directories and not the entire file system. This limits the attack surface.
3. **Implement Secure File Inclusion Methods**
    - **Use Absolute Paths:** Always use absolute paths for file inclusion rather than relying on user-supplied relative paths.
    - **Use PHP Functions Safely:** If using PHP’s `include()` or `require()` functions, ensure that they don’t accept untrusted data. Consider using safer alternatives or explicitly verifying file paths before including them.
4. **Disable Unnecessary PHP Functions**
    - **Disable `include`, `require`, and Related Functions (in Production):** If file inclusion functionality is not needed for your application, disable or restrict the use of functions like `include`, `require`, `include_once`, and `require_once` in your PHP configuration or by modifying `php.ini`.
    - **Disable Dynamic File Execution:** Disable dangerous functions like `eval()`, `assert()`, and others that could allow code execution if LFI is exploited.

## 📚 References

- [File Inclusion/Path traversal (HackTricks)](https://book.hacktricks.xyz/pentesting-web/file-inclusion)
- [Testing for Local File Inclusion (OWASP)](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)
- [Local File Inclusion (LFI): Understanding and Preventing LFI Attacks (Bright Security)](https://brightsec.com/blog/local-file-inclusion-lfi/)
