# ⚙️ Web Parameter Tampering (WTP)

## 📖 Definition

The **Web Parameter Tampering (WTP)** attack is based on the manipulation of parameters exchanged between client and server in order to modify application data, such as user credentials and permissions, price and quantity of products, etc. Usually, this information is stored in cookies, hidden form fields, or URL Query Strings, and is used to increase application functionality and control.

This attack can be performed by a malicious user who wants to exploit the application for their own benefit, or an attacker who wishes to attack a third-person using a [Man-in-the-middle attack](https://owasp.org/www-community/attacks/Man-in-the-middle_attack). In both cases, tools likes Webscarab and Paros proxy are mostly used.

The attack success depends on integrity and logic validation mechanism errors, and its exploitation can result in other consequences including [XSS](https://owasp.org/www-community/attacks/Cross-site_Scripting_/(XSS/)), [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection), file inclusion, and path disclosure attacks.

## 🔍 Discovery

On the **Survey** page, after opening the Developer tools (F12), we inspected the form and saw that we can change the `value` of the `<option>` tags. We try to modify them and it worked when we modify the original value for a value above ten. Then, we selected this new value and we get the flag.

## 🏁 Flag

1. Go on the "Survey" page.
2. Open the Developer tools (F12).
3. Click the "Select" tool and select one of the `<select>` tag and expand it.
4. Change the value of the `value` attribute of one the `<option>` tag (but not the first) for a value above 10.
5. Select in the list the "Grade" you modified and here it is.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

1. **Input Validation and Sanitization**
    - **Strict Input Validation:** Validate all incoming data against strict rules. For example, if a parameter expects numeric values, enforce this rigorously.
    - **Whitelist Approach:** Only allow specific expected values and reject any unexpected or suspicious input.
    - **Escaping Input:** Use proper escaping mechanisms to ensure that manipulated inputs don't execute malicious code or break application logic.
2. **Parameter Integrity Checks**
    - **Use Hashing or Digital Signatures:**
        - Hash sensitive parameters along with a secret key (e.g., HMAC) and validate them on the server side.
    - **Token-Based Integrity:** Use tokens (e.g., CSRF tokens) to verify that requests originate from legitimate users.
3. **Server-Side Validation**
    - **Trust Server-Side Logic:** Never rely solely on client-side checks. Always validate parameters server-side to ensure data integrity.
    - **Cross-Check Parameters:** Implement mechanisms to validate that received parameters match the user’s session state or data stored in the database.
    - **Rate-Limiting and Threshold Checks:** Detect and mitigate repeated or unusual requests targeting specific parameters.
4. **Encrypt Sensitive Parameters**
    - **Encrypt Parameters:** For highly sensitive parameters, use encryption to obscure their values. Only the server should be able to decrypt them.
    - **Avoid Relying on Obfuscation Alone:** Ensure encryption complements other security measures, as encryption can be bypassed if keys are compromised.

## 📚 References

- [Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)
