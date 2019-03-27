import marshal
import struct
import sys
import time
import datetime
import types
import json
import dis
from dis import dis

FLAG_REF = ord('\x80')
TYPE_CODE = ord('c')
TYPE_STRING = ord('s')
TYPE_SMALL_TUPLE = ord(')')
TYPE_INT = ord('i')
TYPE_SHORT_ASCII = ord('z')
TYPE_SHORT_ASCII_INTERNED = ord('Z')
TYPE_REF = ord('r')
TYPE_NONE = ord('N')

REFS_HASH = {}


def parse_code(fp):
    code = int.from_bytes(fp.read(1), 'little')
    code_type = code & ~FLAG_REF
    code_flag = code & FLAG_REF

    idx = len(REFS_HASH)
    if code_flag:
        REFS_HASH[idx] = None

    code_dict = {}
    if code_type == TYPE_CODE:
        code_dict['type'] = 'code'
        code_dict['co_argcount'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_kwonlyargcount'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_nlocals'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_stacksize'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_flags'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_code'] = parse_code(fp)
        code_dict['co_consts'] = parse_code(fp)
        code_dict['co_names'] = parse_code(fp)
        code_dict['co_varnames'] = parse_code(fp)
        code_dict['co_freevars'] = parse_code(fp)
        code_dict['co_cellvars'] = parse_code(fp)
        code_dict['co_filename'] = parse_code(fp)
        code_dict['co_name'] = parse_code(fp)
        code_dict['co_firstlineno'] = int.from_bytes(fp.read(4), 'little')
        code_dict['co_lnotab'] = parse_code(fp)
    elif code_type == TYPE_STRING:
        code_dict['type'] = 'string'

        length = int.from_bytes(fp.read(4), 'little')
        code_dict['length'] = length

        # todo
        value = fp.read(length)
        code_dict['value'] = str(value)

        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SMALL_TUPLE:
        code_dict['type'] = 'tuple'

        size = int.from_bytes(fp.read(1), 'little')
        code_dict['size'] = size

        items = []
        for _ in range(size):
            items.append(parse_code(fp))
        code_dict['items'] = items

        if code_flag:
            REFS_HASH[idx] = code_dict['items']
    elif code_type == TYPE_INT:
        code_dict['type'] = 'long'

        value = int.from_bytes(fp.read(4), 'little')
        code_dict['value'] = value

        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SHORT_ASCII:
        code_dict['type'] = 'unicode'

        size = int.from_bytes(fp.read(1), 'little')
        code_dict['size'] = size

        code_dict['value'] = fp.read(size).decode()

        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SHORT_ASCII_INTERNED:
        code_dict['type'] = 'unicode'

        size = int.from_bytes(fp.read(1), 'little')
        code_dict['size'] = size

        code_dict['value'] = fp.read(size).decode()

        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_REF:
        code_dict['type'] = 'ref'
        code_dict['ref'] = int.from_bytes(fp.read(4), 'little')
        code_dict['value'] = REFS_HASH[code_dict['ref']]
    elif code_type == TYPE_NONE:
        code_dict['type'] = 'none'
    else:
        print(code_type)
    return code_dict


def parse_pyc(file_name):
    pyc_dict = {}
    with open(file_name, 'rb') as fp:
        magic_number = int.from_bytes(fp.read(2), 'little')
        if magic_number >= 3390 and magic_number <= 3394:
            pyc_dict['version'] = 'Python 3.7'
        else:
            print('only support Python 3.7')
            exit(0)
        _ = fp.read(2)
        _ = fp.read(4)
        timestamp = int.from_bytes(fp.read(4), 'little')
        pyc_dict['modified'] = str(datetime.datetime.fromtimestamp(timestamp))
        source_size = int.from_bytes(fp.read(4), 'little')
        pyc_dict['size'] = source_size
        pyc_dict['code'] = parse_code(fp)

    return(pyc_dict)


def main():
    pycObj = parse_pyc('en.pyc')
    print(json.dumps(pycObj, indent=2))

if __name__ == '__main__':
    main()
