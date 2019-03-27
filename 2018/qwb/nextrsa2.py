from pwn import *
import random
import hashlib

#------------round 1--------------

key = dict()

for i in range(0xff):
    for j in range(0xff):
        for k in range(0x1f):
            m = chr(i) + chr(j) + chr(k)
            key[hashlib.sha256(m).hexdigest()[0:8]] = m.encode('hex')

token = "icqemmm"

io = remote("39.107.33.90", 9999)
print io.recvuntil("teamtoken:")
io.sendline(token)
print io.recvuntil("hexdigest()[0:8]=='")
hash8 = io.recv(8)
log.info("Query hash = " + hash8)
print io.recvuntil("('hex')=")
io.sendline(key[hash8])
print io.recv()
#----------------round 2--------------
d = 0x4B80FEEB2506951182788024D66462561ACF32E39366CAD8CE47F2704722FF71
n = 0xc4606b153b9d06d934c9ff86a3be5610266387d82d11f3b4e354b1d95fc7e577

print io.recvuntil('c=')
content = io.recv()
print content
c = int(content[:-5], 16)
log.info("c = " + str(hex(c)))
m = pow(c, d, n)
log.info("m = " + str(hex(m)))
io.sendline(hex(m).replace("L", ""))
io.recv()

#--------------round 3-------------
io.recv()
