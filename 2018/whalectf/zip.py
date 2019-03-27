import binascii
import zlib
import zipfile
import string

f = zipfile.ZipFile("misk7zip.zip", 'r')

smalls = ["%02d" % i for i in range(41)]

smalls_crc = {
    i: "%s" % hex(f.getinfo("miskzip/small_%s.txt" % i).CRC) for i in smalls}

# print(smalls_crc)

dic = string.printable


def crackCrc(crc):
    for a in dic:
        for b in dic:
            for c in dic:
                for d in dic:
                    for e in dic:
                        s = a + b + c + d + e
                        # if crc == (binascii.crc32(s) & 0xffffffff):
                        if crc == binascii.crc32(s.encode("utf-8")):
                            print(s)
                            return s

# crackCrc(0x251dee02)
for i in smalls_crc:
    crc = smalls_crc[i]
    res = crackCrc(crc)
    with open("zip.log", "w") as f:
        f.write(b"%s : %s -> %s" % (i, crc, res))
        f.flush()
