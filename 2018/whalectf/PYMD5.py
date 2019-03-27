# uncompyle6 version 3.2.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (default, Jun 17 2018, 12:46:58)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
# Embedded file name: unVm.py
# Compiled at: 2018-04-17 13:42:14
import md5
md5s = [40872900234340200352311496849171786925L,
        37774871274387226911544626909853297147L,
        136364329640288194110852557127415197202L,
        197102543045186090881257886713375686009L,
        46282790971609926574181364879232245714L,
        199788626591470902691740865303843697496L,
        139155483798021197733301619201494834453L,
        105977393849615850942572250680575701536L,
        103383262965894787541607484291344857033L,
        193549894376121578282270539756256252317L]

flag = "whaleCTF{qAxcx2M3gRf3MGRDFZ2aI6FiNC7Mrm3qEQETD1ew}"
for i in md5s:
    print hex(i)[2:-1]
print 'Can you turn me back to python ? ...'
flag = raw_input('well as you wish.. what is the flag: ')
if len(flag) > 50:
    print 'nice try'
    exit()
if len(flag) % 5 != 0:
    print 'nice try'
    exit()
for i in range(0, len(flag), 5):
    s = flag[i:i + 5]
    print s, int('0x' + md5.new(s).hexdigest(), 16), md5.new(s).hexdigest()
    if int('0x' + md5.new(s).hexdigest(), 16) != md5s[i / 5]:
        print 'nice try'
        exit()

print 'Congratz now you have the flag'
# okay decompiling PYMD5.pyc
