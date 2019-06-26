#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/13, 15:06
"""

import requests as req
import urllib3
import time

urllib3.disable_warnings()

headers = {
    "cookie": "PHPSESSID=vvv; HOST=where_is_my_cat.ichunqiu.com"
}

URL = 'https://106.75.24.88:8006'


def reg(u, p="1234567890"):
    code = ""
    res = req.get(URL + "/register.php", headers=headers, verify=False)
    if res.status_code == 200:
        code = res.headers['date']
        code = int(time.mktime(time.strptime(
            code, "%a, %d %b %Y %H:%M:%S GMT")))
        print(code)
        # TODO: trun
    data = {
        "username": u,
        "password": p,
        "code": code
    }
    res = req.post(URL + "/checkregister.php", data,
                   headers=headers, verify=False)
    if res.status_code == 200:
        print(res.text)
        print(data)


def login(u, p="1234567890"):
    res = req.post(URL + "/checklogin.php", data,
                   headers=headers, verify=False)
    if res.status_code == 200:
        return 1


if __name__ == '__main__':
    reg('test1')
