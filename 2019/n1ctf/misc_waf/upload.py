#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/09/06, 23:03
"""

import hashlib
import requests
import re

req = requests.Session()

URL = 'http://124.156.209.200:5000'


def run_code(code, start=1, end=100000000, pos=0):
    import commands
    res = commands.getstatusoutput(
        "/usr/local/bin/hashpow -p %d -s %d -e %d -c %s" % (pos, start, end, code))
    if len(res) > 1 and res[0] == 0:
        return res[1]
    return False


def getCode():
    res = req.get(URL)
    if res.status_code == 200:
        html = res.content
        m = re.findall(r"'([0-9a-f]{6})'", html)
        if m and len(m) > 0:
            return m[0]
    return False


def upload(captcha):
    data = {
        'team': 'ajGvP1PKxWCqxz6w9RJe43lXlxpldRKuRajgej7laM8XzSC2hC3b7tFyRhND',
        'captcha': captcha
    }
    files = [
        ('waffile', ('waf.php', open('waf.php', 'rb')))
    ]
    res = req.post(URL+'/check', data=data, files=files)
    if res.status_code == 200:
        print(res.content)
        return True
    return False


if __name__ == '__main__':
    code = getCode()
    if code:
        print("[+] Code   : %s" % code)
        code = run_code(code)
        if code:
            print("[+] DeCode : %s" % code)
            if upload(code):
                print("[+] Success")
            else:
                print("[-] Fail to upload")
        else:
            print("[-] Fail to run code")
    else:
        print("[-] Fail to get code")
