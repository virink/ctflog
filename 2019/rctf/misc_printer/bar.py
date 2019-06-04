#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/18, 09:53
"""

import re
from PIL import Image, ImageDraw
image = Image.new('RGB', (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(image)

data = ""
with open("bar.txt", "r") as f:
    data = f.readlines()
for d in data:
    if 'BAR' not in d:
        continue
    d = d.replace('\n', '')[4:]
    t = d.split(", ")
    x = int(t[0])
    y = int(t[1])
    w = int(t[2])
    h = int(t[3])
    draw.line([(x, y), (x+w, y+h)], fill=(0, 0, 0), width=5)
image.show()
