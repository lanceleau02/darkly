import requests
import urllib.request
from bs4 import BeautifulSoup

def script(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")
	for link in soup.find_all('a'):
		if link.get('href') == "README" :
			f = urllib.request.urlopen(url + '/' + link.get('href'))
			myfile = f.read().decode('utf-8')
			if "flag" in myfile:
				print(myfile)
			break
		elif link.get('href') != "../":
			script(url + '/' + link.get('href'))

def main():
	ip = input("Please enter the IP: ")
	print("Searching for the flag...")
	script("http://" + ip + "/.hidden/")

if __name__ == "__main__":
	main()