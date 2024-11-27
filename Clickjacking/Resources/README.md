# 🖱️ Clickjacking

## 📖 Definition

A **Clickjacking Breach** occurs when an attacker manipulates the user interface of a web application to deceive users into performing unintended actions, such as clicking on malicious links or interacting with hidden elements. This type of attack exploits trust and the browser's behavior rather than technical vulnerabilities in the web application's code.

**Key Characteristics of a Clickjacking Breach:**

1. **UI Manipulation:** Attackers alter visible elements of a webpage, such as links or buttons, by overlaying or modifying their underlying attributes.

2. **Deceptive Interaction:** Users are tricked into interacting with malicious content without realizing it, often resulting in unintended actions like visiting harmful sites or sharing sensitive information.

3. **DOM Manipulation:** In cases like the described scenario, attackers leverage browser developer tools or script injection to modify the Document Object Model (DOM) and change attributes such as href.

By exploiting the ability to modify the `href` attribute of social media icons, the attacker redirects clicks to arbitrary destinations, potentially harming users or the website's reputation.

## 🔍 Discovery

While exploring the **Home** page, we go to the footer and see three socials links. So we opened the Developer tools console (F12) and we see that the redirection link (`href`) was present and modifiable:

```HTML
<a href="index.php?page=redirect&amp;site=test" class="icon fa-facebook"></a>
```

So we try to modify it and click on the link and we get the flag.

## 🏁 Flag

1. On the **Home** page, go to the footer.
2. Open the Developer tools (F12).
3. Click the "Select" tool and click one of the three socials logos.
4. In the HTML code, modify the `href` attribute by replacing the name of the social network by whatever you want.
5. Click the logo.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Sanitize and Validate Inputs**
    - Restrict modifications to the DOM that can alter sensitive attributes like `href`.
    - Validate all inputs before rendering links to ensure they conform to expected formats (e.g., only allow specific, pre-approved URLs for social media icons).
- **Disable Inline Modifications**
    - Use Content Security Policy (CSP) headers to restrict inline scripts and unauthorized script execution.
    - Apply readonly attributes to critical DOM nodes in JavaScript to prevent client-side manipulation.
- **Server-Side Integrity Checks**
    - Store allowed href attributes for social media icons in a secure database or configuration file.
    - When rendering the page, dynamically generate the correct URLs server-side to ensure integrity.

## 📚 References

- [Clickjacking (OWASP)](https://owasp.org/www-community/attacks/Clickjacking)
- [Testing for Clickjacking (OWASP)](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/09-Testing_for_Clickjacking)
- [Clickjacking Defense Cheat Sheet (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)