#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/19, 16:06
"""

import requests as req
import json
import os
import binascii

TOKEN = ''
API = 'http://api.ceye.io/v1/records?token={token}&type={type}&filter={filter}'


def getResults(_type="dns", _filter=""):
    if _type not in ["dns", "request"]:
        return False
    url = API.format(token=TOKEN, type=_type, filter=_filter)
    res = req.get(url)
    if res.status_code == 200:
        return res.content.decode("utf-8")
    else:
        return None


def loadResults(fn):
    if not os.path.exists(fn):
        return False
    data = ""
    with open(fn, "r") as f:
        data = f.read()
    # print(data)
    return json.loads(data)


def jsonData(obj):
    p = {}
    for j in obj:
        print(j)
        if 'o_' not in j['name']:
            continue
        kv = j['name'][2:-15].split("_")
        p.update({int(kv[0]): kv[1]})
    res = ""
    sorted(p)
    for i in p:
        print(i)
        res += p[i]
    print(res)
    print(binascii.a2b_hex(bytes(res)))


def readRomoteData(_type="dns", _filter=""):
    data = getResults(_type, _filter)
    obj = json.loads(data)
    return obj['data']


if __name__ == '__main__':
    # obj = loadResults("/Users/virink/Downloads/data.json")
    # jsonData(obj)
    # print(binascii.a2b_hex(bytes(aa)))
    jsonData(readRomoteData())
