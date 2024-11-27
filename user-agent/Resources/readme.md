# User Agent

## 📖 Definition

A **referer header manipulation attack** occurs when an attacker manipulates the HTTP Referer or User-Agent headers to bypass security checks, gain unauthorized access to a system, or perform other malicious actions. The attack is based on tricking the server into accepting a manipulated or false header value that would otherwise be rejected.

**Key Characteristics of a Referer Header Manipulation Attack:**

1. **Header Manipulation:** The attacker changes the Referer and User-Agent headers in the HTTP request to mimic a trusted source. In the given example, the Referer header is set to "https://www.nsa.gov/" and the User-Agent is set to "ft_bornToSec", which are presumably validated by the server to allow further actions.

2. **Bypassing Access Controls:** Many web applications implement basic security checks, such as verifying that requests come from trusted sources or using specific browser identifiers. Manipulating these headers can bypass such controls and trick the system into providing access to restricted resources, such as flags or private data.

3. **Exploitation of Insecure Trust Models:** The system might improperly trust the headers for validation purposes without checking for their authenticity or considering that headers can be easily spoofed. This creates a vulnerability that attackers can exploit.

4. **Possible Outcomes of Such Attacks:**
	- Access to restricted pages or resources by exploiting the header manipulation.
	- Information disclosure, such as flags or sensitive data, by bypassing security mechanisms relying on referer and user-agent checks.
	- Unintended side effects if the web application mistakenly trusts manipulated headers as legitimate.

In summary, referer header manipulation attacks exploit poorly implemented or unvalidated access controls that rely on HTTP headers to determine trustworthiness, allowing attackers to gain access to unauthorized resources.

## 🔍 Discovery

While navigating on the **Home** page, we clicked on the "BornToSec" copyright text in the footer, then we land on a weird page with a music and an Albatroz photo. After some researches, we got the idea to look at the page's source code (Ctrl + U). Further on the page, we see "You must come from : "https://www.nsa.gov/"." and "Let's use this browser : "ft_bornToSec". It will help you a lot.". The first advice tell us that the request must come from `https://www.nsa.gov/` (`Referer`) and the browser used must have `ft_bornToSec` as `User-Agent`. So after many tries, we find this command:

```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" 'http://<ip>/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' | grep flag
```

This command uses the curl tool to send an HTTP request to a specified URL, while manipulating the `User-Agent` and `Referer` headers. The `-A "ft_bornToSec"` option sets a custom `User-Agent` header, making the request appear as if it's coming from a specific browser identified as "ft_bornToSec". The `-e "https://www.nsa.gov/"` option sets the `Referer` header to simulate that the request is coming from the NSA's official website. After making the request, the output is filtered with `grep flag` to search for and display any lines containing the word "flag", indicating the possible presence of a flag or sensitive information on the targeted page.

## 🏁 Flag
 
1. Execute this command `curl -A "ft_bornToSec" -e "https://www.nsa.gov/" 'http://10.13.248.194/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' | grep flag`

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

