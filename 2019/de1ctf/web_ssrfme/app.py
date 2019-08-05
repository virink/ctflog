
#! /usr/bin/env python
# encoding=utf-8
from flask import Flask
from flask import request
import socket
import hashlib
import urllib
import sys
import os
reload(sys)
sys.setdefaultencoding('latin1')

app = Flask(__name__)

# secert_key = os.urandom(16)
secert_key = '1234567890123456'

# print(secert_key)


class Task:
    def __init__(self, action, param, sign, ip):
        self.action = action
        self.param = param
        self.sign = sign
        self.sandbox = md5(ip)
        if(not os.path.exists(self.sandbox)):  # SandBox For Remote_Addr
            os.mkdir(self.sandbox)

    def Exec(self):
        print("EXEC %s" % self.action)
        result = {}
        result['code'] = 500
        if (self.checkSign()):
            if "scan" in self.action:
                tmpfile = open("./%s/result.txt" % self.sandbox, 'w')
                resp = scan(self.param)
                if (resp == "Connection Timeout"):
                    result['data'] = resp
                else:
                    print resp
                    tmpfile.write(resp)
                    tmpfile.close()
                result['code'] = 200
            if "read" in self.action:
                f = open("./%s/result.txt" % self.sandbox, 'r')
                result['code'] = 200
                result['data'] = f.read()
            if result['code'] == 500:
                result['data'] = "Action Error"
        else:
            result['code'] = 500
            result['msg'] = "Sign Error"
        return result

    def checkSign(self):
        # if (getSign(self.action, self.param) == self.sign):
        s = getSign(self.action, self.param)
        if (s == self.sign):
            return True
        else:
            return False


def getSign(action, param):
    r = hashlib.md5(secert_key + param + action).hexdigest()
    print("[+] getSign : %s" % (secert_key + urllib.quote(param) + action))
    print("[+] getSign : key=%s param:%s action:%s sign:%s" %
          (secert_key, urllib.quote(param), action, r))
    return r
    # return hashlib.md5(secert_key + param + action).hexdigest()

# generate Sign For Action Scan.


@app.route("/geneSign", methods=['GET', 'POST'])
def geneSign():
    param = urllib.unquote(request.args.get("param", ""))
    action = "scan"
    return getSign(action, param)


@app.route('/De1ta', methods=['GET', 'POST'])
def challenge():
    param = urllib.unquote(request.args.get("param", ""))
    action = urllib.unquote(request.cookies.get("action"))
    sign = urllib.unquote(request.cookies.get("sign"))
    ip = request.remote_addr
    if(waf(param)):
        return "No Hacker!!!!"
    task = Task(action, param, sign, ip)
    return task.Exec()


@app.route('/')
def index():
    # return f.open("code.txt", 'r').read()
    # ip = request.remote_addr
    def checkSign(self):
        if (getSign(self.action, self.param) == self.sign):
            return True
        else:
            return False
    return '1'


def scan(param):
    socket.setdefaulttimeout(1)
    try:
        print(param)
        return urllib.urlopen(param).read()[:50]
    except:
        return "Connection Timeout"


def md5(content):
    return hashlib.md5(content).hexdigest()


def waf(param):
    check = param.strip().lower()
    if check.startswith("gopher") or check.startswith("file"):
        return True
    else:
        return False


if __name__ == '__main__':
    app.debug = True
    app.run()
