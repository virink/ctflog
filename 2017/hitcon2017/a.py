#!/usr/local/env python2

import requests as req


def fff():
    a = [
        'nc', '-l', '-p', '99'
    ]
    # echo $@

if __name__ == '__main__':
    # http://52.199.204.34/sandbox/74d6a4204acd22312217b711ea48059d/a
    # u = 'http://52.199.204.34/sandbox/62bae9d5f1e2aa652017d1e6ad596d60/a'
    # u = 'http://52.199.204.34/sandbox/62bae9d5f1e2aa652017d1e6ad596d60/b'
    # u = 'http://52.199.204.34/sandbox/62bae9d5f1e2aa652017d1e6ad596d60/e'
    u = 'http://52.199.204.34/sandbox/62bae9d5f1e2aa652017d1e6ad596d60/'
    for i in range(1, 256):
        # print chr(i)
        try:
            res = req.get(url=u + chr(i))
            if res.status_code == 200:
                print chr(i)
        except Exception as e:
            print chr(i)
            # print e
            pass
