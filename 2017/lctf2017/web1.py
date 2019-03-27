#!/usr/bin/python
# coding:utf-8

import requests
import sys
import urllib
from base64 import b64decode as dec
from base64 import b64encode as enc

url = 'http://127.0.0.1:8011/cbc.php'


# def Test(x):
#     s = 'guest'
#     ​for i in xrange(0, len(s), 16):
#         print s[i:i + 16]


def Pwn(s):
    global url
    s = urllib.quote_plus(enc(s))
    req = requests.get(url, cookies={'settings': s}).content
    #   if req.find('works') != -1:
    print req
    #  else:
    #     print '[-] FAIL'


def GetCookie(name):
    global url
    d = {
        'username': 'admin',
        'password': 'admin'
    }
    h = requests.post(url, data=d, headers={
                      'Content-Type': 'application/x-www-form-urlencoded'}).headers
    h = dict(h)
    print(h['Set-Cookie'][h['Set-Cookie'].find('token') + 6:])
    if h.has_key('Set-Cookie'):
        h = dec(urllib.unquote_plus(
            h['Set-Cookie'][h['Set-Cookie'].find('token') + 6:]))
        #h = urllib.unquote_plus(h['Set-Cookie'][9:])
        # print h
        return h
    else:
        print '[-] ERROR'
        sys.exit(0)
    # guess
    # admin

exploit = 'admin'  # Test Success
# Test(exploit)
cookie = GetCookie(exploit)
print(cookie)
pos = 10  # test case success
val = chr(ord('X') ^ ord("'") ^ ord(cookie[pos]))
exploit = cookie[0:pos] + val + cookie[pos + 1:]
Pwn(exploit)
