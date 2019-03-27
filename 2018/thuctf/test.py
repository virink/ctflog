import marshal
import tempfile
import os
import sys
import re
from dis import dis


co_code = b't\x00j\x01d\x01d\x02\x83\x02}\x00|\x00t\x00d\x01<\x00|\x00d\x03k\x02r*d\x04|\x00\x9b\x00d\x05\x9d\x03}\x01n\x0cd\x04|\x00\x9b\x00d\x06\x9d\x03}\x01t\x02j\x03j\x01d\x07d\x08\x83\x02}\x02d\t|\x02k\x06s\\d\n|\x02k\x06s\\d\x0b|\x02k\x06rdt\x04d\x0c\x83\x01S\x00d\r|\x02\x9b\x00d\x0e|\x01\x9b\x00d\x0f\x9d\x05}\x03t\x04|\x03\x83\x01S\x00'
co_consts = (None, 'username', 'guest', 'admin', 'Hi,', '! This is your flag: THUCTF{Do_n0t_s4ve_4uth_1nfo_1n_fl4sk_s3ss10n}', '! Only admin can get the flag!', 'msg', '', '(', ')', 'config',
             'Illegal request!', '\\n    {% extends "layout.html" %}\\n    {% block body %}\\n    \\t<h2 class="form-signin-heading">', '</h2>\\n    \\t<h4>', '</h4>\\n    {% endblock %}\\n    ')
co_varnames = ['username', 'info', 'msg', 'template']
co_names = ('session', 'get', 'request', 'args', 'render_template_string')


global stack
stack = ['']


def readData(filename):
    res = b''
    with open('_t_%s' % filename, 'rb') as f:
        res = f.read()[16:]
    return res


def readFile(fp):
    fp.seek(0)
    res = fp.read()
    return res


def readFileLines(fp):
    fp.seek(0)
    res = fp.readlines()
    return res


def getDisData(code):
    tmp = tempfile.TemporaryFile(mode='w+t')
    dis(code, file=tmp)
    res = readFileLines(tmp)
    tmp.close()
    return res


def emmmm(line):
    global stack
    _len = len(line)
    pos = line[0]
    token = line[1]
    index = int(line[2]) if _len >= 3 else None
    _ = line[3] if _len >= 4 else None
    # print(pos, token, index, _)
    tmp = ''
    if token == 'LOAD_GLOBAL':
        tmp = co_names[index]
    elif token == 'LOAD_ATTR':
        # tmp = 'getattr("%s", "%s")' % (stack.pop(), co_names[index])
        tmp = '%s.%s' % (stack.pop(), co_names[index])
    elif token == 'LOAD_CONST':
        tmp = co_consts[index]
    elif token == 'CALL_FUNCTION':
        args = []
        for i in range(index):
            args.append("'%s'" % stack.pop())
        func = stack.pop()
        tmp = '%s(%s)' % (func, ','.join(args))
    elif token == 'STORE_FAST':
        # tmp = co_varnames[index]
        # co_varnames[index] = stack.pop()
        tmp = '%s=%s' % (co_varnames[index], stack.pop())
    elif token == 'LOAD_FAST':
        tmp = co_varnames[index]
    elif token == 'STORE_SUBSCR':
        TOS = stack.pop()
        TOS1 = stack.pop()
        TOS2 = stack.pop()
        # stack.append(TOS2)
        # stack.append(TOS1)
        # stack.append(TOS)
        tmp = "%s['%s']=%s" % (TOS1, TOS, TOS2)
        # TOS1[TOS] = TOS2
        print("STORE_SUBSCR : %s['%s']=%s" % (TOS1, TOS, TOS2))
    elif token == 'COMPARE_OP':
        op1 = stack.pop()
        op2 = stack.pop()
        tmp = "if '%s' %s %s:" % (op1, _[1:-1], op2)
    elif token == 'POP_JUMP_IF_FALSE':
        tmp = 'else:\r\tjump %s' % (index)
        tmp = ''
    elif token == 'FORMAT_VALUE':
        _t = index & 0x03
        # print(stack)
        # sys.exit(0)
        op1 = stack.pop()
        op2 = stack.pop()
        if _t == 0x00:
            tmp = '"%s%%s" %% %s' % (op2, op1)
    elif token == 'BUILD_STRING':
        args = []
        for i in range(index):
            args.append("%s" % stack.pop())
        print("---" * 10)
        print(args)
        print("---" * 10)
        # sys.exit(0)
        tmp = ''
    return tmp

if __name__ == '__main__':
    # dis(co_code)
    _co_code = getDisData(co_code)
    # print(_co_code)
    for line in _co_code:
        line = line.replace('\n', '').split(' ')
        line = [i for i in line if i != '' and i != '>>']
        tmp = emmmm(line)
        if tmp:
            print(tmp)
            stack.append(tmp)
    print('=' * 50)
    print('\n'.join(stack))
