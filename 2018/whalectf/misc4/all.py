from capstone import *
import glob
from PIL import Image

md = Cs(CS_ARCH_X86, CS_MODE_32)

for fn in glob.glob("*.bmp"):

    img = Image.open(fn)
    pixels = img.load()
    w, h = img.size

    s = ""
    for y in range(h - 1, -1, -1):
        for x in range(w):
            if pixels[x, y][0] == 0x90 or pixels[x, y][2] == 0x80:
                s += ''.join([chr(_) for _ in pixels[x, y][::-1]])

    lines = []
    for inst in md.disasm(s, 0):
        lines += ["0x%x:\t%s\t%s" % (inst.address, inst.mnemonic, inst.op_str)]

    print fn

    ecx = 0
    out = ""
    for l in lines:
        if 'byte ptr [ecx]' in l:
            tmp = l.strip().split(', ')[1]
            if tmp.startswith("0x"):
                tmp = int(tmp, 16)
            else:
                tmp = int(tmp)

            if 'add' in l:
                ecx += tmp
            elif 'sub' in l:
                ecx -= tmp

        elif 'int\t0x80' in l:
            out += chr(ecx)

    print out

    break

    # whaleCTF{c3dbbf0298eceb3edcd6d2505fd8d30d}
