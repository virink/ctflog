import requests

URL = 'http://54.223.247.98:8090/'
req = requests.session()


def getId(_id):
    data = {
        'text': _id
    }
    headers = {
        'Referer': "http://54.223.247.98:8090/shop_items.php?id=ODE2ZXY5dDQwSXNLZ0FSTkhWMGlreXlnR1hXNCtkNDlDdTN3c2NHVFlwQkEyZw=="
    }
    res = req.post(URL + '/share.php', data=data, headers=headers)
    if res.status_code == 200:
        return res.content


def test(p):
    res = req.get(URL + '/shop_items.php?id=' + p)
    if res.status_code == 200:
        return res.content

if __name__ == '__main__':
    req = requests.session()
    payload = "34534"
    _id = getId(payload)
    print _id
    res = test(_id)
    print res[res.find("/user/login.php") + 120:]
