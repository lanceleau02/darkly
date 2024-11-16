# 🍪 Cookies

## 📖 Definition

**Cookies** are small pieces of data stored on a user's device by a web browser at the request of a website. They are used to store information about the user's interactions with the website, such as preferences, login credentials, or session data, to enhance the browsing experience. Cookies can be categorized as follows:

- **Session Cookies:** These are temporary and deleted once the user closes their browser. They are used to maintain a session, such as keeping a user logged in while navigating a site.

- **Persistent Cookies:** These remain on the user's device for a set period or until manually deleted. They are used to remember preferences or login details for future visits.

- **First-Party Cookies:** Created by the website the user is visiting, they support essential functionality like language preferences or shopping carts.

- **Third-Party Cookies:** Set by domains other than the one the user is visiting, these are often used for tracking and advertising purposes across different sites.

Cookies play a critical role in web functionality but can raise privacy concerns, especially when used for tracking user behavior across sites. Most modern browsers provide tools to manage and control cookies.

## 🔍 Discovery

By opening the Developer Tools window (F12 or Shift + Ctrl + I), we checked the cookies used on the website ("Application" tab) and there is only one named `I_am_admin` with a value of `68934a3e9455fa72420237eb05902327`. After identifying the cipher as a MD5 encryption, thanks to [dCode](https://www.dcode.fr/cipher-identifier), we decrypted it and obtained `false`. Then, we just encrypted the `true` word to MD5 and modified the cookie using this code (use `allow pasting` if needed):

```JavaScript
document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09"
```

Then, we refreshed the page and got the flag!

## 🏁 Flag

<u>**Using the console:**</u>

1. Open the Developer tools (F12 or Shift + Ctrl + I)
2. Display the cookie using `document.cookie`
3. Change the cookie with (use `allow pasting` if needed):

```JavaScript
document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09"` 
```

4. Refresh the page

<u>**Using the Application tab:**</u>

1. Open the Developer tools (F12 or Shift + Ctrl + I)
2. Go on the "Application" tab
3. Click on "Cookies" and then on the website IP
4. Double-click on the value and paste `b326b5062b2f0e69046810717534cb09`
5. Refresh the page

<u>**Using a browser extension:**</u>

1. Download [Cookie-Editor](https://cookie-editor.com/)
2. Go on the BornToSec website
3. Open extension
4. Click the cookie
5. Modify its value by `b326b5062b2f0e69046810717534cb09`
6. Click on "Save"
7. Refresh the page

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Relying solely on client-side data for authentication:** store sensitive user data, including roles, on the server side instead. Use a server-side session to manage privileges, with the session ID stored in a secure cookie.
- **Secure session cookies:** replace the current cookie-based approach with secure session management: use a unique and unpredictable session ID, store all session-related data on the server and ensure cookies are marked as: **HttpOnly** (prevents JavaScript access to cookies and mitigating XSS risks), **Secure** (ensures cookies are transmitted only over HTTPS) and **SameSite** (protects against CSRF attacks by restricting cross-site cookie access).
- **Weak or reversible hashes:** if hashing is required, use strong, modern cryptographic hashing algorithms such as SHA-256 or better. However, hashing alone is not enough; combine it with other techniques to prevent tampering.
- **Digital signatures for cookies:** protect cookies from tampering by using a digital signature mechanism: sign the cookie with a secret server-side key and validate the signature on the server whenever the cookie is used.
- **Proper role validation:** validate user roles and privileges on the server side for every sensitive action. Do not trust client-side indicators, such as a cookie, to authorize actions.
- **Sensitive cookie data:** encrypt the contents of cookies with a robust encryption algorithm and securely manage encryption keys. However, encryption should not replace proper server-side validation.

## 🧰 Toolbox

- [dCode](https://www.dcode.fr/)
- [Cookie-Editor](https://cookie-editor.com/)

## 📚 References

- [Session Management Cheat Sheet (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [Cookies Hacking (HackTricks)](https://book.hacktricks.xyz/pentesting-web/hacking-with-cookies)
