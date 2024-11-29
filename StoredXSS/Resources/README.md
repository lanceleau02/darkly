# ❓ Feedback

## 📖 Definition

**Cross-Site Scripting (XSS)** is a type of security vulnerability that occurs when an attacker is able to inject malicious scripts (typically JavaScript) into a web page viewed by other users. This can allow the attacker to execute arbitrary code in the context of a user's browser, steal session cookies, deface content, or perform other malicious actions.

**Types of XSS:**

1. **Stored XSS:** The malicious script is stored on the server (e.g., in a database) and then executed when other users load the page containing that script.

2. **Reflected XSS:** The script is reflected off the server, typically through user input, without being stored.

3. **DOM-based XSS:** The vulnerability exists in the client-side code, and the attack is executed through manipulation of the DOM by the attacker.

This breach is a **Reflected XSS** one, since the input (e.g., the word "script") is immediately reflected back in the response.

## 🔍 Discovery

After some researches, we discover the existence of the XSS breaches, so we started to try different inputs, in the "Name" and "Message" fields, until we try `script` and then we got the flag. Afterwards, we also discover that the breach is a little bit bugged because the `a` and `e` inputs also display the flag...

## 🏁 Flag

1. Go on the **Feeback** page
2. Write the "script" word in the "Name" field

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Input Validation:** ensure that all user inputs are sanitized. For example, check that input fields that expect text do not contain HTML tags or JavaScript code.
- **Output Encoding:** properly encode user inputs before reflecting them back into the page, so that any special characters (like `<`, `>`, or `"`), which could be interpreted as part of HTML or JavaScript, are treated as plain text.
- **Content Security Policy (CSP):** implement a strict CSP to prevent the execution of inline scripts.
- **Use Framework Security Features:** many modern frameworks (e.g., React.js, Angular, Vue.js...) automatically escape user input to prevent XSS. Using them can help prevent this kind of issue.

## 📚 References

- [Cross Site Scripting (XSS) (OWASP)](https://owasp.org/www-community/attacks/xss/)
- [Cross-site scripting (PortSwigger)](https://portswigger.net/web-security/cross-site-scripting)


