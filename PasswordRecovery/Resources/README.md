# 🔑 Password Recovery

## 📖 Definition

A **password recovery breach** occurs when an attacker exploits vulnerabilities in the password recovery process of a system to bypass authentication or gain unauthorized access to an account. This can involve manipulating the system’s functionality, such as altering form fields or requests during the password recovery procedure.

**Key Characteristics of a Password Recovery Breach:**

1. **Exploiting Recovery Mechanisms:** Attackers manipulate the password recovery process, such as by editing form data or sending modified requests, to gain access to user accounts without proper authentication.

2. **Client-Side Manipulation:** This type of breach often relies on manipulating HTML code, JavaScript, or form elements on the client side using browser developer tools. For example, changing values in hidden form fields or submitting altered data can bypass security checks.

3. **Insufficient Validation or Protection:** The breach occurs when the system fails to properly validate or secure its password recovery process, allowing attackers to set arbitrary values for sensitive fields, such as user IDs or password reset tokens.

If successfully executed, a password recovery breach can allow an attacker to reset passwords, lock out legitimate users, or gain unauthorized access to accounts.

## 🔍 Discovery

To discover this breach, we go to the **Sign in** page and click on "I forgot my password". The fact that there is just a "Submit" button was strange so we decided to inspect the code's page thanks to the Developer tools (F12). We see this line:

```HTML
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

The `value`of the `input` tag is clearly defined so we try to change it, click on the "Submit" button and we get the flag!

## 🏁 Flag

1. Go on the **Sign in** page
2. Click on "I forgot my password"
3. Open the Developer tools (F12)
4. Click the "Select" tool and click on the "Submit" button
5. In the HTML code, replace the content of the `value` attribute by whatever you want
6. Click on the "Submit" button

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

1. **Server-Side Validation and Verification**
	- **Validate Input on the Server:** Never trust data that comes from the client side. Always verify user input on the server-side, such as ensuring that the user requesting a password reset is indeed the owner of the account.
	- **Secure Password Reset Tokens:** Generate strong, random password reset tokens that are time-sensitive and difficult to predict. Ensure tokens are validated on the server and linked to a specific user account to prevent tampering.
2. **Use of HTTPS for Secure Communication**
	- **Encrypt All Traffic:** Ensure that all communication, especially related to password recovery, happens over HTTPS (SSL/TLS) to protect sensitive information from being intercepted or altered during transmission.
3. **Implement Multi-Factor Authentication (MFA)**
	- **Require MFA for Password Recovery:** Enable multi-factor authentication during the password recovery process. For example, after the user enters their email for password reset, send a one-time code via SMS or email that must be entered to continue the recovery process.
	- **Risk-Based Authentication:** If suspicious activity is detected (e.g., unusual IP addresses or locations), challenge the user with additional verification steps such as answering security questions or submitting a one-time password (OTP).
4. **Limit the Number of Password Recovery Attempts**
	- **Implement Rate Limiting and Captchas:** To prevent brute-force attacks or rapid repeated attempts to exploit the recovery process, use rate limiting and CAPTCHA mechanisms. After a certain number of failed attempts, lock the user out temporarily or require additional verification to ensure that the request is legitimate.
5. **Protect Against Client-Side Manipulation**
	- **Use Nonces and Hidden Fields with Proper Security:** Use nonces (one-time tokens) in form submissions to ensure that requests are genuine and not manipulated by an attacker. These tokens should be validated on the server before processing any password reset request.
	- **Sanitize HTML Forms:** Make sure that all form fields, including hidden fields, cannot be tampered with by disabling editing or preventing manipulation via developer tools. This can include setting strict content security policies (CSP) to limit script injection.

## 📚 References

- [Forgot Password Cheat Sheet (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [Exploring Password Reset Vulnerabilities and Security Best Practices (Vaadata)](https://www.vaadata.com/blog/exploring-password-reset-vulnerabilities-and-security-best-practices/)