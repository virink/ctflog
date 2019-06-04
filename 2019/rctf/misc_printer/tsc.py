#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/18, 09:53
"""

import re
from PIL import Image, ImageDraw


def hex2binStr(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


image = Image.new('RGB', (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(image)

# BAR x,y,w,h
# data = ""
# with open("bar.txt", "r") as f:
#     data = f.readlines()
# for d in data:
#     if 'BAR' not in d:
#         continue
#     d = d.replace('\n', '')[4:]
#     t = d.split(", ")
#     x = int(t[0])
#     y = int(t[1])
#     w = int(t[2])
#     h = int(t[3])
#     draw.line([(x, y), (x+w, y+h)], fill=(0, 0, 0), width=5)
#     print(t)

#        x,   y,  width,  height, mode
# BITMAP 138, 75, 26,     48,     1,(or)
x = 138
y = 75
_x = 26 * 8
_y = 48 * 8
data = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc7fffffffffffffffffffffffffffffffffffffffffffffffffffffffe38fffffffffffffffffffffffffffffffffffffffffffffffffffffffdff7ffffffffffffffffffffffffffffffffffffffffffffffffffffff9ff3ffffffffffffffffffffffffffffffffffffffffffffffffffffff9ff3fffffffffffff9ffefbffc7ffffffe1fff8fffffffc3ffffffffff9ff3ff8ffffffffff0ffefbff39ff007f9c7fe72ffffff3c3fc07fffff87e78463f803ff01f0ffe7bfefefff7ff3f3f9f8fffffeff3ffbffffffc01fa3f9ffbfffe7f9ffe71fcfe7ff7ff7f9f9fcfffffeffbffbfffffffc07e7f9ffbfffe7ffffc71f9ff3ff7feff9f3fcfffffeffbffbffffffffe7e7f8ffbfffe7ffffd75f9ff3ff7ffffcf3fcfffffe7ffffbffffffffe7e7f9ffbfffe7ffffd35f9ff3ff7ffffcf3fcfffffe3ffffbfffffff80fe7f9ffbfffe7ffffd2cf9ff3ff7ffffcf3fcffffff07fffbfffffff7cfe7f3ffbfffe7ffffb2cf9ff3ff7fe000f3fcffffffc1fffbffffffe7e7e7c7ffbfffe7ffffbacf9ff3ff7fe7fcf3fcfffffff87ffbffffffe7e7e03fffbfffe7ffffb9ef9ff3ff7fe7fcf3fcfffffffe7ffbffffffefe7e7ffffbfffe7ffffb9e79ff3ff7fe7f9f3fcfffffeff3ffbffffffefe7e7f9ffbfffe7ffff79e7cfe7ff7ff3f9f9f8fffffeff3ffbffffffe7e7f7f1ffbfffe7f1ff79e7efcfff7ff3f3f9f0fffffe7f7ffbffffff27eff3f3ffbfffe7f0fe38e3f39fff7ffce7fc04fffffe1cfff9ffffff019ff9e7ffbfffe7f1fffffffc7fff7fff1fffbcfffffee3fff87fffffbe7ffe1fffbffe00ffffffffffffff7ffffffffcffffffffffffffffffffffffffffbfffe7ffffffffffffff7ffffffffcffffffffffffffffffffffffffffbfffe7ffffffffffffff7ffffffffcffffffffffffffffffffffffffffbfffe7ffffffffffffff7ffffffffcffffffffffffffffffffffffffffbfe7e7ffffffffffffff7ffffffffcfffffffffff3ffffffffffffffffbfe7efffffffffffffff7ffffffffcfffffffffff1ffffffffffffffffbfe7cfffffffffffffff03fffffffc3ffffffffff1ffffffffffffffff81f03fffffffffffffff3ffffffffcfffffffffffbffffffffffffffff9ffffff"
bitmap = ""
for i in range(0, len(data), 2):
    # if (i+1) % 13 == 0:
    #     print(i)
    #     bitmap += "\n"
    t = data[i:i+2]
    tt = hex2binStr(t)
    bitmap += tt
print(bitmap)
# image.show()
