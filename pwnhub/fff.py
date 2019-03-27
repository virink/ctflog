#!/usr/bin/python
#-*- encoding: utf-8 -*-

import md5
import sys
import requests
import re
import time

req = requests.Session()


def mx(str):
    m1 = md5.new()
    m1.update(str)
    return m1.hexdigest()


def captcha(s):
    t = time.time()
    print 'Run md5 for key ...'
    # print 'Start time : ', int(t)
    for x in range(1000000, 100000000):
        a = mx(str(x))
        if a[:6] == s:
            print 'The code is : ', x
            print 'The captcha is : ', a
            print 'Used time : ', int(time.time() - t), 's'
            return x
    return False


def get(url):
    # res = req.get(url, cookies=cookie)
    res = req.get(url)
    if res.status_code == 200:
        html = res.content
        res = re.findall(r'substr\(md5\(captcha\), 0, 6\)=(.{6})', html)
        return res[0]
    else:
        return False


def post(url, data):
    # url = 'http://52.80.32.116/2d9bc625acb1ba5d0db6f8d0c8b9d206/login.php'
    # res = req.post(url, data, cookies=cookie)
    res = req.post(url, data)
    if res.status_code == 200:
        print res.cookies
        return res.content


def login(data):
    url = 'http://52.80.32.116/2d9bc625acb1ba5d0db6f8d0c8b9d206/login.php'
    ca = ""
    print 'Getting captha key ...'
    c = get(url)
    if not c:
        print 'not captcha key', '\n'
        return 0
    print 'The captcha key is : ', c
    ca = captcha(c)
    if not ca:
        print "md5 for key error", '\n'
        return 0
    data['captcha_md5'] = str(ca)
    print 'Post data is : '
    print data, '\n'
    print 'Post data ...'
    res = post(url, data)
    if res:
        print res, '\n'
    # print 'Over'


if __name__ == '__main__':
    # print 'Running ...'
    # u = []  # "admin'\"><img src=x onerror=alert(/xss/) />"
    # p = "123456"
    # if len(sys.argv) == 3:
    #     u = sys.argv[1]
    #     p = sys.argv[2]
    # data = dict(username=u, password=p, captcha_md5="", submit="Submit")
    # login(data)
    print captcha('fc8264')
