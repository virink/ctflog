#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/13, 11:00
"""

import base64

x = []

with open('give_to_player', 'r') as f:
    x = f.readlines()
x = [a.strip() for a in x]


def xorr(pwd, key):
    result = []
    for j in range(len(key)):
        result.append(chr(ord(pwd[j]) ^ ord(key[j])))  # 跟KEY异或回去就是原明文
    result = ''.join(result)
    return result


_r = ""
for i in x:
    _x = i.split(":")
    mi = base64.b64decode(_x[1])
    if 'flag' in _x[0]:
        print(xorr(_r, mi))
        break
    _r = xorr(mi, _x[0])
