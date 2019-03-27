#!/usr/bin/env python2
# encoding=utf8

from collections import Counter
from mail_send import send_mail

ip = []
statusCode = []


def toDeal(filename):
    with open(filename, 'r') as f:
        logs = f.readlines()
        for log in logs:
            ip.append(log.split()[0])
            statusCode.append(log.split()[8])

    logAll = '日志总数：' + str(len(logs))
    ipUV = '独立 IP：' + str(list(set(ip)))
    ipNumber = 'IP出现次数：' + str(dict(Counter(ip)))
    codeNumber = '状态码出现次数：' + str(dict(Counter(statusCode)))
    content = logAll + '\n' + ipUV + '\n' + ipNumber + '\n' + codeNumber
    send_mail('Pwnhub Nginx Report', content)

if __name__ == '__main__':
    toDeal('/usr/local/var/log/nginx/access.log')
