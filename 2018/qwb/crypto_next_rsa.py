#/usr/bin/env python2
# coding:utf-8

import socket
import re
import hashlib
import random
import time
import sys
import math


teamtoken = 'icq94b161318dd2542504ae977743e7e'

HOST = '39.107.33.90'
PORT = 9999


def fuck():
    # 定义socket类型，网络通信，TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    data = s.recv(1024)
    data = s.recv(1024)
    s.sendall(teamtoken)
    data = s.recv(1024)
    data = s.recv(1024)
    print(data)
    m = re.findall(r'hexdigest\(\)\[0:8\]==\'([\w]{8})\'', str(data))
    print(m)
    res = fuck1(m[0])
    if res:
        s.sendall(res)
    data = s.recv(1024)
    data = s.recv(1024)
    print(data)

    s.close()


def fuck1(m):
    for i in range(0, 0xff + 1):
        for j in range(0, 0xff + 1):
            for k in range(0, 0x1f + 1):
                x = chr(i) + chr(j) + chr(k)
                h = hashlib.sha256(x).hexdigest()[0:8]
                if h == m:
                    return x.encode('hex')
    return 0


def fuck2(n, e, c):
	m = math.pow(int(c), e, n)
    m = hex().rstrip("L")
    # c = (m ^ e) % n
    # i = 1
    # while 1:
    #     x = i * n + c
    #     if x
    #     i += 1
    # m = 1
if __name__ == '__main__':
	n = 0xc4606b153b9d06d934c9ff86a3be5610266387d82d11f3b4e354b1d95fc7e577
	e = 0x10001
	c = 0x5c46c0cadd1da1859fa011ac8586a6100a3fdcb4d619a1970dff4164d98a1f9
    fuck2()
