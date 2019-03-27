import requests as req

URL = 'http://virink.audit.virzz.com/'


def get():
    res = req.get(url=URL + '/index.php')
    if res.status_code == 200:
        h = dict(res.headers)
        print(res.content)
        return h['Date']


def get2(v):
    res = req.get(url=URL + 'index.php?t=' + v)
    if res.status_code == 200:
        # print(res.url)
        print(res.content)

if __name__ == '__main__':
    d = get()
    print(d)
    get2(d)
    get2(d)
    get2(d)
