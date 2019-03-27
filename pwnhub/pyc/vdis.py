# -*- coding: utf-8 -*-
"""Disassembler of Python byte code into mnemonics."""

import sys
import vtypes

from vopcode import *
from vopcode import __all__ as _opcodes_all

__all__ = ["dis", "disassemble", "distb", "disco",
           "findlinestarts", "findlabels"] + _opcodes_all
del _opcodes_all

_have_code = (vtypes.MethodType, vtypes.FunctionType, vtypes.CodeType,
              vtypes.ClassType, type)


def b2n(b):
    return ord(b[0]) + ord(b[1]) * 0x100


def dis(x=None):
    """Disassemble classes, methods, functions, or code.
    分解类、方法、函数或代码。
    With no argument, disassemble the last traceback.
    在没有参数的情况下，分解最后一个回溯。
    """
    if x is None:
        distb()
        return
    if isinstance(x, vtypes.InstanceType):
        x = x.__class__
    if hasattr(x, 'im_func'):
        x = x.im_func
    if hasattr(x, 'func_code'):
        x = x.func_code
    if hasattr(x, '__dict__'):
        items = x.__dict__.items()
        items.sort()
        for name, x1 in items:
            if isinstance(x1, _have_code):
                print "Disassembly of %s:" % name
                try:
                    dis(x1)
                except TypeError, msg:
                    print "Sorry:", msg
                print
    elif hasattr(x, 'co_code'):
        disassemble(x)
    elif isinstance(x, str):
        disassemble_string(x)
    else:
        raise TypeError, \
            "don't know how to disassemble %s objects" % \
            type(x).__name__


def distb(tb=None):
    """Disassemble a traceback (default: last traceback).
    分解回溯（默认：最后回溯）。"""
    if tb is None:
        try:
            tb = sys.last_traceback
        except AttributeError:
            raise RuntimeError, "no last traceback to disassemble"
        while tb.tb_next:
            tb = tb.tb_next
    disassemble(tb.tb_frame.f_code, tb.tb_lasti)


def disassemble(co, lasti=-1):
    """Disassemble a code object.
    分解代码对象"""
    code = co.co_code
    labels = findlabels(code)
    linestarts = dict(findlinestarts(co))
    n = len(code)
    i = 0
    extended_arg = 0
    free = None
    while i < n:
        # add try
        msg = ''
        try:
            c = code[i]
            op = ord(c)
            if i in linestarts:
                if i > 0:
                    print
                print "line : %3d\n   " % linestarts[i],
            else:
                print '   ',

            if i == lasti:
                print '-->',
            else:
                print '   ',
            if i in labels:
                print '>>',
            else:
                print '  ',
            res = ''
            try:
                res = opname[op]
            except:
                res = "<%s>"
            print repr(i).rjust(4),
            print res.ljust(20),
            i = i + 1
            if op >= HAVE_ARGUMENT:
                oparg = ord(code[i]) + ord(code[i + 1]) * 256 + extended_arg
                # print '\r\n->', oparg, '<-'
                extended_arg = 0
                i = i + 2
                if op == EXTENDED_ARG:
                    extended_arg = oparg * 65536L
                print repr(oparg).rjust(5),
                if op in hasconst:
                    msg = 'hasconst'
                    # print '(' + repr(co.co_consts[oparg]) + ')',
                    try:
                        print '(' + repr(co.co_consts[oparg]) + ')',
                    except:
                        print '(' + repr(co.co_consts[b2n(oparg)]) + ')',
                elif op in hasname:
                    msg = 'hasname'
                    # print '(' + co.co_names[oparg] + ')',
                    try:
                        print '(' + co.co_names[oparg] + ')',
                    except:
                        print '(' + co.co_names[b2n(oparg)] + ')',
                elif op in hasjrel:
                    msg = 'hasjrel'
                    print '(to ' + repr(i + oparg) + ')'
                    print '(to ' + repr(i + b2n(oparg)) + ')',
                elif op in haslocal:
                    msg = 'haslocal'
                    # print '(' + co.co_varnames[oparg] + ')',
                    try:
                        print '(' + co.co_varnames[oparg] + ')',
                    except:
                        print '(' + co.co_varnames[b2n(oparg)] + ')',
                elif op in hascompare:
                    msg = 'hascompare'
                    # print '(' + cmp_op[oparg] + ')',
                    try:
                        print '(' + cmp_op[oparg] + ')',
                    except:
                        print '(' + cmp_op[b2n(oparg)] + ')',
                elif op in hasfree:
                    msg = 'hasfree'
                    if free is None:
                        free = co.co_cellvars + co.co_freevars
                        # print '(' + free[oparg] + ')',
                        try:
                            print '(' + free[oparg] + ')',
                        except:
                            print '(' + free[b2n(oparg)] + ')',
        except Exception, e:
            print
            print '=' * 20
            print 'error opcode:', e
            print '-->', msg, oparg, '<--'
            print '=' * 20
        print


def disassemble_string(code, lasti=-1, varnames=None, names=None,
                       constants=None):
    labels = findlabels(code)
    n = len(code)
    i = 0
    while i < n:
        c = code[i]
        op = ord(c)
        if i == lasti:
            print '-->',
        else:
            print '   ',
        if i in labels:
            print '>>',
        else:
            print '  ',
        print repr(i).rjust(4),
        print opname[op].ljust(15),
        i = i + 1
        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i + 1]) * 256
            i = i + 2
            print repr(oparg).rjust(5),
            if op in hasconst:
                if constants:
                    # print '(' + repr(constants[oparg]) + ')',
                    try:
                        print '(' + repr(constants[oparg]) + ')',
                    except:
                        print '(' + repr(constants[b2n(oparg)]) + ')',
                else:
                    print '(%d)' % oparg,
            elif op in hasname:
                if names is not None:
                    # print '(' + names[oparg] + ')',
                    try:
                        print '(' + names[oparg] + ')',
                    except:
                        print '(' + names[b2n(oparg)] + ')',
                else:
                    print '(%d)' % oparg,
            elif op in hasjrel:
                print '(to ' + repr(i + oparg) + ')'
                print '(to ' + repr(i + b2n(oparg)) + ')',
            elif op in haslocal:
                if varnames:
                    # print '(' + varnames[oparg] + ')',
                    try:
                        print '(' + (varnames[oparg]) + ')',
                    except:
                        print '(' + (varnames[b2n(oparg)]) + ')',
                else:
                    print '(%d)' % oparg,
            elif op in hascompare:
                # print '(' + cmp_op[oparg] + ')',
                try:
                    print '(' + (cmp_op[oparg]) + ')',
                except:
                    print '(' + (cmp_op[b2n(oparg)]) + ')',
        print

"""
XXX For backwards compatibility
向后兼容性
"""
disco = disassemble


def findlabels(code):
    """Detect all offsets in a byte code which are jump targets.
    检测跳转目标的字节码中的所有偏移量。
    Return the list of offsets.
    返回偏移量列表
    """
    labels = []
    n = len(code)
    print "code len : ", n
    i = 0
    while i < n:
        try:
            c = code[i]
            op = ord(c)
            i = i + 1
            if op >= HAVE_ARGUMENT:
                oparg = ord(code[i]) + ord(code[i + 1]) * 256
                i = i + 2
                label = -1
                if op in hasjrel:
                    label = i + oparg
                elif op in hasjabs:
                    label = oparg
                if label >= 0:
                    if label not in labels:
                        labels.append(label)
        except Exception, e:
            print
            print '=' * 20
            print 'findlabels:', e
            print '--> op:', op, 'oparg:', oparg, '<--'
            print '=' * 20
    return labels


def findlinestarts(code):
    """Find the offsets in a byte code which are start of lines in the source.
    查找字节码中的偏移量，这是源代码行的起点。
    Generate pairs (offset, lineno) as described in Python/compile.c.
    （偏移，产生对线）的描述在Python/compile.c
    """
    byte_increments = [ord(c) for c in code.co_lnotab[0::2]]
    line_increments = [ord(c) for c in code.co_lnotab[1::2]]
    lastlineno = None
    lineno = code.co_firstlineno
    addr = 0
    for byte_incr, line_incr in zip(byte_increments, line_increments):
        if byte_incr:
            if lineno != lastlineno:
                yield (addr, lineno)
                lastlineno = lineno
            addr += byte_incr
        lineno += line_incr
    if lineno != lastlineno:
        yield (addr, lineno)


def _test():
    """Simple test program to disassemble a file.
    简单的文件删除测试程序"""
    if sys.argv[1:]:
        if sys.argv[2:]:
            sys.stderr.write("usage: python dis.py [-|file]\n")
            sys.exit(2)
        fn = sys.argv[1]
        if not fn or fn == "-":
            fn = None
    else:
        fn = None
    if fn is None:
        f = sys.stdin
    else:
        f = open(fn)
    source = f.read()
    if fn is not None:
        f.close()
    else:
        fn = "<stdin>"
    code = compile(source, fn, "exec")
    dis(code)

if __name__ == "__main__":
    _test()
