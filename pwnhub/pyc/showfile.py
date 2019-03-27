#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import vdis
import marshal
import struct
import sys
import time
import types


def show_file(fname):
    f = open(fname, "rb")
    f.seek(8)
    code = marshal.load(f)
    print '=' * 20
    print(dir(code))
    print '=' * 20
    show_code(code)


def show_code(code, indent=''):
    old_indent = indent
    print "%s<code>" % indent
    indent += '   '
    print "%s<argcount> %d </argcount>" % (indent, code.co_argcount)
    print "%s<nlocals> %d</nlocals>" % (indent, code.co_nlocals)
    print "%s<stacksize> %d</stacksize>" % (indent, code.co_stacksize)
    print "%s<flags> %04x</flags>" % (indent, code.co_flags)
    # show_hex("code", code.co_code, indent=indent)
    print "%s<names> %r</names>" % (indent, code.co_names)  # 所有符号名称集合
    print "%s<varnames> %r</varnames>" % (indent, code.co_varnames)
    print "%s<freevars> %r</freevars>" % (indent, code.co_freevars)
    print "%s<cellvars> %r</cellvars>" % (indent, code.co_cellvars)
    print "%s<filename> %r</filename>" % (indent, code.co_filename)
    print "%s<name> %r</name>" % (indent, code.co_name)
    print "%s<firstlineno> %d</firstlineno>" % (indent, code.co_firstlineno)
    print "%s<consts>" % indent
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent + '   ')
        else:
            print "   %s%r" % (indent, const)
    print "%s</consts>" % indent
    show_hex("lnotab", code.co_lnotab, indent=indent)
    print "%s<dis>" % indent
    vdis.disassemble(code)
    print "%s</dis>" % indent
    print "%s</code>" % old_indent


def show_hex(label, h, indent):
    h = h.encode('hex')
    if len(h) < 60:
        print "%s<%s> %s</%s>" % (indent, label, h, label)
    else:
        print "%s<%s>" % (indent, label)
        for i in range(0, len(h), 60):
            print "%s   %s" % (indent, h[i:i + 60])
        print "%s</%s>" % (indent, label)

show_file(sys.argv[1])
