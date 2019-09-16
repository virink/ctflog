#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/09/15, 17:23
"""

data = ""

with open("scrapy/vkrce.egg", 'rb') as f:
    data = f.read()

print([ord(data[i]) for i in range(len(data))])
