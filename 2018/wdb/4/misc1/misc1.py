
from PIL import Image

ss = ""

for i in range(576):
    im = Image.open("p%03d.png" % (i + 1))
    pix = im.load()
    x = (i % 24) * 10
    y = (i / 24) * 10
    z = pix[x, y]
    ss += "0" if z == (0, 255, 0, 255) else "1"

xx = ""
for i in range(int(len(ss) / 8)):
    xx += chr(int(ss[i * 8:(i + 1) * 8], 2))
print(xx)
