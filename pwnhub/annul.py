#!/usr/bin/env python3

# import commands
import socket

HOST = '52.80.154.150'
PORT = 9999
SETP = 1

NAME = b'vvv'


def dealRes(_socket, res):
    print(res)
    if b'WRONG SELECT!' in res:
        return 1
    # Give me your name!
    if b'Give me your name!' in res or NAME in res:
        _socket.sendall(NAME)
        res = _socket.recv(1024 * 4)
        print(res)
        return 0
    if b'\nS)how my money\nP)rint my packets\nG)et more packet\nB)ye\n' in res:
        _socket.sendall(b"S")
        return 0
    if b'distributing' in res or b'Come on' in res or b'R)ename' in res:
        return 0

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_client.sendall(b'vvv')
try:
    # tcp_client.bind(('192.168.1.6', 11560))
    tcp_client.connect((HOST, PORT))
except socket.error:
    print('fail to setup socket connection')
else:
    res = tcp_client.recv(1024 * 4)
    r = 0
    while len(res) > 0 and r == 0:
        r = dealRes(tcp_client, res)
        res = tcp_client.recv(1024 * 4)
tcp_client.close()
