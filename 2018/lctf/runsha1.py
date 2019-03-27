#!/bin/env python
# -*- encoding: utf-8 -*-

import hashlib
import sys


def md5x(s):
    hash = hashlib.sha1()
    hash.update(bytes(s, encoding='utf-8'))
    return hash.hexdigest()


def run(code):
    start = 10000000
    end = 100000000
    # print('Runing...')
    while start <= end:
        res = md5x(str(start))[:len(code)]
        if res == code:
            # print start
            return start
        start += 1


if __name__ == '__main__':
    while 1:
        c = input("$ ")
        if c == "q":
            break
        else:
            print(run(c))
