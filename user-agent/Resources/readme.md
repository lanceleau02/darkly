# User Agent

1. Go on the "Albatroz" page and do CTRL+U to see the source code of the page
2. Further on the page, we can see "You must come from : "https://www.nsa.gov/"." and "Let's use this browser : "ft_bornToSec". It will help you a lot."
3. Execute this command `curl -A "ft_bornToSec" -e "https://www.nsa.gov/" 'http://10.13.248.194/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' | grep flag`