#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

__info__ = {
    "desc": "Output a tar file by script",
    "version": "1.0",
    "usage": "tarfile filename content_name content_data"
}


def tarfile(content_name='test.php', content_data='test'):
    if len(content_name) > 100:
        print 'content_name error'
        return
    t_name = content_name + '\x00' * (100 - len(content_name))
    t_mode = '0000664\x00'
    t_uid = '0001750\x00'
    t_gid = '0001750\x00'
    t_size = '00000000004\x00'
    t_mtime = '01274124644\x00'
    t_chksum = ''
    t_typeflag = '0'
    t_linkname = '\x00' * 100
    t_magic = 'ustar\x32'
    t_version = '\x32\x00'
    t_uname = 'root' + '\x00' * (32 - 4)
    t_gname = 'root' + '\x00' * (32 - 4)
    t_devmajor = '\x00' * 8
    t_devminor = '\x00' * 8
    t_prefix = '\x00' * 155
    t_padding = '\x00' * 12
    t_block = content_data + '\x00' * (512 - len(content_data))
    if len(content_data) < 1000:
        s = str(len(content_data))
        if len(content_data) > 0 and len(content_data) < 10:
            t_size = '0000000000' + s + '\x00'
        elif len(content_data) > 10 and len(content_data) < 100:
            t_size = '000000000' + s + '\x00'
        elif len(content_data) > 100:
            t_size = '00000000' + s + '\x00'
        else:
            return 0
    _a = t_name + t_mode + t_uid + t_gid + t_size + t_mtime
    _b = t_typeflag + t_linkname + t_magic + t_version + t_uname + \
        t_gname + t_devmajor + t_devminor + t_prefix + t_padding
    _t = _a + _b
    _sum = 0
    for j in _t:
        _sum += ord(j)
    t_chksum = '0' * (8 - len(str(oct(_sum + 256)))) + str(oct(_sum + 256))
    return _a + t_chksum + _b + t_block + '\x00' * 512


def saveToFile(filename, tarData):
    f = open(filename, 'wb')
    f.write(tarData)
    f.close()


def run(fn, cn, cd):
    filename = fn + ".tar"
    content_name = cn or "virink.txt"
    content_data = cd or "virink"
    print 'Runing...'
    saveToFile(filename, tarfile(content_name, content_data))
    if os.path.exists(filename):
        print os.path.join("./", filename)
    else:
        print False

if __name__ == '__main__':
    run('9981', '2333', 'ddddd')
