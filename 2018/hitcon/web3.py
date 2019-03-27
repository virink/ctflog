from Crypto.Cipher import DES
import urlparse

ENCRPYTION_KEY = 'megnnaro'


def decrypt(s):
    try:
        data = s.decode('hex')
        cipher = DES.new(ENCRPYTION_KEY, DES.MODE_ECB)
        data = cipher.decrypt(data)
        print(data)
    except Exception as e:
        print(e.message)
        return {}


if __name__ == '__main__':
    decrypt('2e7e305f2da018a2cf8208fa1fefc238')
    decrypt(
        '4b596c43212b27b7c948390491293dd24f6f5f3b635ddb984c1c23f162d392ccf900061d8b6338771d8feb029243ed633882b1034e8789849136472bd93ffe2dfd8017786de53c1785a67bbbcecad1c78b096aa66c3ff957aaa3bb913d35c75f')
    decrypt(
        'be24b0e6a4592fab1f8a22a342e43575e547d2499523d59754ba9923e44088052a5be3ba8bae2a94')
