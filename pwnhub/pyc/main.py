#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import sys
import os
import marshal
import vdis as dis
import vopcode


def pycf(fn):
    with open(fn, 'rb') as f:
        f.seek(8)
        mf = marshal.load(f)
        print '=' * 20
        print(mf)
        print '=' * 20
        dis.dis(mf)


if __name__ == '__main__':
    arg = sys.argv[1]
    pycf(arg)
