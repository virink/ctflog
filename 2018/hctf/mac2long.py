base = [str(x) for x in range(10)] + [chr(x)
                                      for x in range(ord('A'), ord('A')+6)]


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])


def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


def bin2dec(string_num):
    return str(int(string_num, 2))


def mac2long(mac):
    macArr = mac.split(":")
    longStr = ""
    for m in macArr:
        t = hex2bin(m)
        longStr = "%s%08s" % (longStr, t)
    longStr = longStr.replace(" ", "0")
    print(bin2dec(longStr))


if __name__ == '__main__':
    mac = '12:34:3e:14:7c:62'
    mac2long(mac)
