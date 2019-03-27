# -*- coding: utf-8 -*-
from PIL import Image
import re
import base64
flag = ''
for i in range(576):
    im = Image.open("p%03d.png" % (i + 1))
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    tmp = pix[(i % 24) * 10 + 5, (i / 24) * 10 + 5][:-1]
    if tmp == (255, 0, 255):
        flag += '1'
    elif tmp == (0, 255, 0):
        flag += '0'

bb = re.findall(r'.{8}', flag)
print bb
str1 = ""
for b in bb:
    str1 += chr(int(b, 2))
print str1
