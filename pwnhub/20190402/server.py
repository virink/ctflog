#!/usr/bin/env python3

import zlib
from Crypto.Cipher import AES
import sys
import os
from hashlib import md5

flag = open("flag.txt").read()
while True:
    data = input()
    data = "message: %s, flag: %s" % (data, flag)
    compressed = zlib.compress(data.encode())
    if len(compressed) % 16:
        compressed += b"\x00" * (16 - len(compressed) % 16)
    encrypted = AES.new(
        md5(flag.encode()).digest(), AES.MODE_CBC, os.urandom(16)
    ).encrypt(compressed)
    print(encrypted.hex())
