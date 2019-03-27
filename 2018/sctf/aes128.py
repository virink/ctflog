# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os
import zlib

c = ""
with open("./fuzz_web3/login.php", 'rb') as f:
    c = f.read()[16:]
print
c = ''.join([chr(ord(i) ^ 0x9a) for i in c])

with open("./fuzz_web3/login.php.bak", 'wb') as f:
    f.write(c)
# c = zlib.decompress(c)
# fu =
# print zlib.MAX_WBITS, 'compress : ', zlib.compress(" 1").encode("hex")
# print len(c), c, c.encode("hex")
# c = zlib.decompress(c)
# c = zlib.decompress(c, -zlib.MAX_WBITS)
# c = zlib.decompress(c)
decompress = zlib.decompressobj()
c = decompress.decompress(c)
print len(c), c  # , c.encode("hex")
print
# padding算法
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(0)


def unpad(s):
    print 's:', s[-1], -ord(s[-1])
    return s[0:-ord(s[-1])]
key = pad('YP68y3FsMDc6TvRgghq')  # the length can be (16, 24, 32)
cipher = AES.new(key)

decrypted = cipher.decrypt(pad(c))
print decrypted
print

# text = '<?php phpinfo(); ?>'
# text = pad(text)
# print text
# print
# encrypted = cipher.encrypt(text)
# print len(encrypted), encrypted
# decrypted = cipher.decrypt(encrypted)
# # print decrypted
# # decrypted = unpad(decrypted)
# print len(decrypted), decrypted  # will be 'to be encrypted'
