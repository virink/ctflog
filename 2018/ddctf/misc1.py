# d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1b2e2e5e2b5b4e4b8b7e6e1e1b6b9e4b5e3b8b1b1e3e5b5b6b4b1b0e4e6b2fd

from binascii import *

ori = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1b2e2e5e2b5b4e4b8b7e6e1e1b6b9e4b5e3b8b1b1e3e5b5b6b4b1b0e4e6b2fd"
_bin = a2b_hex(ori)

for i in range(1, 0xff):
    tmp = ""
    for j in _bin:
        tmp += chr(ord(j) - i)
    if 'DDCTF' in tmp:
        print(tmp)
        break
