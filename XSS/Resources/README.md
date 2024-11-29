# ❌ Cross Site Scripting (XSS)

## 📖 Definition

**Cross-Site Scripting (XSS)** attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws, see: [Types of Cross-Site Scripting](https://owasp.org/www-community/Types_of_Cross-Site_Scripting).

## 🔍 Discovery

While navigating on the **Home** page, we noticed the NSA logo was clickable. So we tried to click on it and we land on a page with the same logo. After a little digging, we saw this in the URL:

```URL
http://<ip>/index.php?page=media&src=nsa
```

And particularly this part: `&src=nsa` because it means that we can replace the `nsa` parameter with a malicious payload. After many researches, we found this payload:

```URL
data:text/html;base64,PHNjcmlwdD5hbGVydCgncGF5bG9hZCcpPC9zY3JpcHQ+
```

But what does this gibberish mean? Ok, let's breakdown it:

1. **Data URI Scheme:**
	- The `data`: scheme allows embedding inline data, such as HTML, CSS, or JavaScript, directly in a URL.
	- In this case, `data:text/html;base64,` decodes to an inline HTML/JavaScript snippet.
2. **Base64 Payload Decoded:**
	- The base64-encoded string `PHNjcmlwdD5hbGVydCgncGF5bG9hZCcpPC9zY3JpcHQ+` decodes to: `<script>alert('payload')</script>`
	- This injects a `<script>` tag into the page, causing the browser to execute `alert('payload')`.

If the server or client-side code directly uses the parameter without sanitization (e.g., inserting it into a webpage or evaluating it), the script runs in the context of the affected domain.

## 🏁 Flag

1. Go on the "Home" page
2. Click on the NSA logo
3. In the URL, replace the "nsa" by `data:text/html;base64,PHNjcmlwdD5hbGVydCgncGF5bG9hZCcpPC9zY3JpcHQ+`

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

1. **Input Validation and Sanitization**
	- **Validate Input:** Check all incoming parameters to ensure they match the expected format. Reject or sanitize inputs that:
		- Contain potentially malicious content (e.g., `<script>`, `data:`, `javascript:`).
		- Use prohibited protocols like `data:`.
	- **Whitelist Validation:** Only allow values from a predefined, safe list.
	- **Remove Dangerous Characters:** Strip characters like `<`, `>`, `"` if they are unnecessary for the parameter.
2. **Output Encoding**
	- **HTML Encoding:**
		- Encode all user-supplied data before inserting it into the HTML response.
		- For example, if the input is `data:text/html...`, encode it so it displays as text rather than executing.
	- **Contextual Encoding:**
		- Use the right encoding for the context (e.g., JavaScript, HTML, or URL encoding).
3. **Implement a Content Security Policy (CSP)**
	- A CSP restricts the types of scripts and content that can run on your site, mitigating XSS and injection attacks.
	- In this case, the CSP will block inline JavaScript, such as the malicious `<script>` tag.
4. **Restrict Dangerous URI Schemes**
	- Block the use of unsafe protocols like `data:`, `javascript:`, or `vbscript:` in URL parameters.
	- Server-side validation should explicitly disallow these protocols:
```python
if user_input.startswith("data:") or user_input.startswith("javascript:"):
	return "Invalid URL"
```
5. **Avoid Reflecting Unsanitized Input**
	- Ensure that URL parameters are not directly reflected in the HTML output without sanitization or escaping.

## 📚 References

- [Cross Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Types of XSS](https://owasp.org/www-community/Types_of_Cross-Site_Scripting)