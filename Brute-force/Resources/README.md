# 💪 Bruteforce

---

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

---

## 🔍 Discovery

On the **Signin** page, we try several `username:password` combinations after realizing that the `username` and `password` are directly filled in the URL in this format: `username=<username>&password=<password>`.
So, at this point, we can code a little Python script to test all the possibilities with the `root` username. Why with this username? Because we test it first and by chance it was the good one.

---

## ⚙️ Reproduction

**1. The fastest way:**

1. Go on the **Signin** page
2. In the username field, type `root`
3. In the password field, type `shadow`

**2. Using the script:**

1. In a terminal, run `python script.py <ip>`
2. Enter the IP of the website

