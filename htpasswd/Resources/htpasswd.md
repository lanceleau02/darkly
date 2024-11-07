#  htpasswd

1. Go on http://10.13.248.201/robots.txt and see `Disallow: /whatever`
2. So go on http://10.13.248.201/whatever/
3. Download the `htpasswd` file
4. Decrypt the password using the MD5 algorithm
5. Go on http://10.13.248.201/admin/
6. Type `root` as username and `qwerty123@` as password and here it is
