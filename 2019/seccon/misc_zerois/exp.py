from pwn import *
from sympy import *
from sympy.abc import x


def fuck(v):
    return solve([eval(v)], [x])


p = remote('zerois-o-reiwa.seccon.jp', 23615)

res = p.recvline()
print(res)
for i in range(100):
    res = p.recvline()
    print(res)
    res = res.replace("?", 'x')[2:]
    try:
        res = fuck(res)
        print(res)
        r = str([res[i] for i in res][0])
    except:
        try:
            res = fuck(res)
            print(res)
            r = str([res[i] for i in res][0])
        except:
            pass
    print(r)
    p.sendline(r)
    res = p.recvline()
    print(res)
p.interactive()
