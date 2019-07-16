#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/07/05, 11:44

# Login
# curl -c sess http://127.0.0.1:6666/login -d "username=virink666&password=virink666"

curl -s -b sess http://127.0.0.1:6666/flag -H "X-Forwarded-For: 127.0.0.1"