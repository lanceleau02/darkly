# ⚙️ Web Parameter Tampering (WTP)

## 📖 Definition
A Client-Side Manipulation Attack is a type of security breach in which an attacker manipulates data or behavior on the client-side (the user's browser) in order to gain unauthorized benefits, typically by altering or bypassing the intended functionality of a website.

Key Characteristics of a Client-Side Manipulation Attack:

Exploiting Client-Side Vulnerabilities: The attacker takes advantage of features or elements rendered in the browser, such as HTML, JavaScript, or CSS, to modify form data, URLs, or settings before they are submitted to the server.

Manipulating Form Data: In this specific case, the attacker manipulates the value of an HTML <option> tag (within a <select> dropdown) by changing the value attribute to a higher value than intended. This can allow the user to select an option that would normally be restricted or unavailable, such as bypassing a grade restriction.

Lack of Proper Server-Side Validation: The attack relies on the absence of proper validation on the server-side. If the server does not verify that the modified input is valid or authorized, the attacker can successfully alter the outcome of a form submission, such as gaining access to restricted grades or information.

Manipulation Without Server Interaction: This kind of attack occurs entirely on the client side and does not require direct interaction with the server, although the altered data is eventually sent to the server for processing.

Common Attack Vectors:

Form Field Manipulation: Changing values in form fields (such as dropdown menus or hidden fields).
URL Manipulation: Changing URL parameters or query strings to gain unauthorized access to resources.
Cookie Manipulation: Modifying cookie values to impersonate other users or bypass security.
This kind of attack is typically mitigated through proper server-side validation, ensuring that all user inputs are checked for validity before they influence the application's behavior.

1. Go on the "Survey" page
2. Open the Developer tools (F12)
3. Click the "Select" tool and select one of the `<select>` tag and expand it
4. Change the value of the `value` attribute of one the `<option>` tag (but not the first) for a value above 10
5. Select in the list the "Grade" you modified and here it is

https://owasp.org/www-community/attacks/Web_Parameter_Tampering