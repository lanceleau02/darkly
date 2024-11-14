# 💪 Bruteforce

## 📖 Definition

A **brute-force attack** is a method used to gain unauthorized access to a system, network, or encrypted data by systematically trying all possible combinations of credentials or keys until the correct one is found. This type of attack relies on sheer computational power and persistence, making it one of the simplest, yet most resource-intensive and time-consuming, attack methods.

**Key Characteristics of a Brute-Force Attack:**

1. **Trial-and-Error Approach:** Attackers use software to automatically generate and test millions or billions of potential passwords, usernames, or encryption keys, often using algorithms that speed up this trial-and-error process.

2. **No Subtlety or Sophistication:** Unlike other types of cyber attacks that may rely on exploiting specific vulnerabilities, brute-force attacks don't require intricate knowledge of the target system. The approach is purely a numbers game: try everything until something works.

3. **Dependent on Computational Power:** The speed and feasibility of a brute-force attack are heavily influenced by the processing power available to the attacker. More powerful systems (or botnets of compromised machines working together) can test combinations faster.

4. **Types of Brute-Force Attacks:**

	- **Simple Brute-Force Attack:** Every possible combination of characters is tested, regardless of the target's characteristics.
	- **Dictionary Attack:** Attackers use a predefined list of likely passwords, often based on commonly used passwords or information known about the target.
	- **Hybrid Attack:** Combines a dictionary attack with variations on each entry, such as adding numbers or symbols to commonly used words.

## 🔍 Discovery

On the **Signin** page, we try several `username:password` combinations after realizing that the `username` and `password` are directly filled in the URL in this format: `username=<username>&password=<password>`.
So, at this point, we can code a little Python script to test all the possibilities with the `root` username. Why with this username? Because we test it first and by chance it was the good one. For the dictionary, we use [this one](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) from GitHub.

## ⚙️ Reproduction

**1. The fastest way:**

1. Go on the **Signin** page
2. In the username field, type `root`
3. In the password field, type `shadow`

**2. Using the script:**

1. In a terminal, run `python script.py <ip>`

## 🔧 Patch

A lot of defense measures can be taken but here are the main ones:

- **Password Complexity:** Requiring complex, long passwords makes brute-forcing more time-consuming.

- **Account Lockouts:** Locking an account after several failed attempts can thwart brute-force efforts.
- **Multi-Factor Authentication (MFA):** Adding an additional layer of security (e.g., a verification code sent to the user) can stop a brute-force attack even if a password is successfully guessed.
- **Rate Limiting and Captchas:** These limit the number of attempts an attacker can make in a given timeframe, slowing down or deterring brute-force attempts.

Here is a chart to estimate the time it can takes a hacker to brute force your password:

[](https://images.squarespace-cdn.com/content/5ffe234606e5ec7bfc57a7a3/1719499399309-7FRIR5QNH5P4VHC1AGGP/Hive+Systems+Password+Table+-+2024+Rectangular.png?format=1500w&content-type=image%2Fpng)