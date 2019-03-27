def fuck(s):
    res = []
    _h = "`'%\\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%"
    _f = "[(({}<[])<<({}<[]))::~(~(({}<[])<<({}<[]))<<({}<[]))]"
    for i in s:
        res.append(_h + brainfuckize(ord(i)))
    print('`[' + ','.join(res) + ']`' + _f)


def brainfuckize(nb):
    if nb in [-2, -1, 0, 1]:
        return ["~({}<[])", "~([]<[])", "([]<[])",  "({}<[])"][nb + 2]
    if nb % 2:
        return "~%s" % brainfuckize(~nb)
    else:
        return "(%s<<({}<[]))" % brainfuckize(nb / 2)

if __name__ == '__main__':
    fuck('test,emmmmm')
