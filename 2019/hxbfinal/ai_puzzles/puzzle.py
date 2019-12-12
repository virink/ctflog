#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/11/26, 22:05
"""

import sys
import os
import cv2
import time
from PIL import Image


def cutFlagImage(puzzles_path, NUM=20):
    try:
        os.removedirs(puzzles_path)
    except OSError:
        pass
    try:
        os.mkdir(puzzles_path)
    except OSError:
        pass
    flag_image = 'flag.png'
    image = Image.open(flag_image)
    width, height = image.size
    # print(width, height)
    w = int(width / NUM)
    h = int(height / NUM)
    # print(w, h)
    boxs = []
    for y in range(0, NUM):
        for x in range(0, NUM):
            boxs.append((x*w, y*h, (x+1) * w, (y+1)*h))
    # print(boxs)
    # [(0, 0, 84, 52), (84, 0, 168, 52), (168, 0, 252, 52)
    for box in boxs:
        crop = image.crop(box)
        crop.save('./%s/p%d.png' % (puzzles_path, index), 'PNG')
        index += 1


def cutOriginImage(filepath, vx, vy):
    try:
        os.removedirs('datas')
    except OSError:
        pass
    try:
        os.mkdir('datas')
    except OSError:
        pass
    try:
        os.remove('results.png')
    except OSError:
        pass
    im = Image.open(filepath)
    origin_width, origin_height = im.size
    put("[+] origin_width = %d origin_height = %d\n" %
        (origin_width, origin_height))
    xn = round(origin_width / vx)
    yn = round(origin_height / vy)
    index = 1
    maps = [[0] * (xn) for i in range(yn)]
    for y in range(0, yn):
        for x in range(0, xn):
            maps[y][x] = index
            crop = im.crop((x*vx, y*vy, (x+1) * vx, (y+1)*vy))
            crop.save('./datas/p'+str(index) + '.png', 'PNG')
            index += 1
    return maps


# ======

# 差异值哈希算法
def dhash(image_part_file, resize=32):
    resize_height, resized_width = resize, resize+1
    img = cv2.imread(image_part_file)
    image = cv2.resize(img, (resized_width, resize_height),
                       interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    hash_list = []
    for i in range(resize_height):
        for j in range(resized_width-1):
            if gray[i, j] > gray[i, j + 1]:
                hash_list.append('1')
            else:
                hash_list.append('0')
    return ''.join(hash_list)


# 计算两个哈希值之间的差异
def campHash(hash1, hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def walk(path):
    results = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            results.append(name)
    return results


if __name__ == '__main__':
    # cutFlagImage()

    # flag_part_image = './puzzles/p1.png'
    # origin_image = 'origin.png'
    put = sys.stdout.write

    if len(sys.argv) < 3:
        put(
            "[!] Usage: %s source_image part_image [size]\n" % sys.argv[0])
        sys.exit(1)

    _t = time.time()

    origin_image = sys.argv[1]
    flag_part_image = sys.argv[2]
    p_size = 32
    if len(sys.argv) > 3:
        p_size = int(sys.argv[3])

    puzzles_path = os.path.dirname(flag_part_image)

    # Get Flag Part Image Size
    im = Image.open(flag_part_image)
    part_width, part_height = im.size
    put("[+] Get Flag Part Image Size:\n")
    put("[+] part_width = %d part_height = %d\n" % (part_width, part_height))

    maps = cutOriginImage(origin_image, part_width, part_height)

    # Read In Mem
    put("[+] Read Image Hash In Mem:\n")
    puzzles = {}
    datas = {}
    for p in walk(puzzles_path):
        puzzles[p] = dhash('./%s/%s' % (puzzles_path, p), p_size)
    puzzles_len = len(puzzles)
    pMaps = {}
    i = 1
    put("[+] Compare Image Hash:\n")
    for rows in maps:
        for p in rows:
            # print(i)
            bfb = int(i/puzzles_len*100)
            put("\r[*] %s %d/100" % ("=" * bfb, bfb))
            i += 1
            hs = dhash('./datas/p%s.png' % p, p_size)
            ds = 10000
            for pn in puzzles:
                d = campHash(hs, puzzles[pn])
                if d == 0:
                    pMaps[p] = pn
                    del puzzles[pn]
                    break
                elif d < ds:
                    ds = d
                    pMaps[p] = pn
    put("\r[+] %s 100/100\n" % ("=" * 100))

    # Paste Image
    img = Image.open(origin_image)
    origin_w, origin_h = img.size
    target_image = Image.new('RGB', (origin_w, origin_h))
    put("[+] Paste Image:\n")
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            fn = "%s/%s" % (puzzles_path, pMaps[maps[y][x]])
            box = (x * part_width, y * part_height, (x+1)
                   * part_width, (y+1) * part_height)
            # print(box)
            im = Image.open(fn)
            target_image.paste(im, box)
    target_image.save('results' + '.png', 'PNG')

    put("[+] Use Time: %s\n" % (time.time() - _t))
    put("[+] Success:\n")
    os.system("open results.png")
