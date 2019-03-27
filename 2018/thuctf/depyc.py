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


def readData(filename):
    res = None
    with open(filename, 'rb') as f:
        res = f.read()
    return res


def write_pyc(file_name, headPos, endPos):
    pyc_data = None
    _head = None
    _end = None
    tmp = readData(file_name)
    _head = tmp[:headPos]
    _end = tmp[endPos:]
    pyc_code_data = fake_code()
    with open("de_%s" % file_name, 'wb') as fp:
        fp.write(_head + pyc_code_data + _end)
    # return(pyc_data)


def _fake_code_tuple(data):
    var_data = eval(data)
    print(var_data)
    print(len(var_data))
    _result = b''
    for _data in var_data:
        _tmp = b''
        # print(_data, type(_data))
        if isinstance(_data, str):
            _tmp = TYPE_SHORT_ASCII_INTERNED.to_bytes(
                1, byteorder='big') + (len(_data)).to_bytes(1, byteorder='big') + _data.encode("utf-8")
        else:
            # print(type(_data))
            _tmp = TYPE_NONE.to_bytes(1, byteorder='big')
            # sys.exit(0)
        print(_tmp)
        _result += _tmp
    return _result


def fake_code():
    code_type = TYPE_CODE.to_bytes(1, byteorder='big')

    # function ses
    co_argcount = (int(readData('_t_co_argcount'))
                   ).to_bytes(4, byteorder='big')

    co_kwonlyargcount = (int(readData('_t_co_kwonlyargcount'))
                         ).to_bytes(4, byteorder='big')

    co_nlocals = (int(readData('_t_co_argcount'))).to_bytes(4, byteorder='big')

    co_stacksize = (int(readData('_t_co_argcount'))
                    ).to_bytes(4, byteorder='big')

    co_flags = (int(readData('_t_co_argcount'))).to_bytes(4, byteorder='big')

    _co_code_type = readData('_t_co_code')
    co_code = TYPE_STRING.to_bytes(
        1, byteorder='big') + (len(_co_code_type)).to_bytes(4, byteorder='big') + _co_code_type

    _co_consts = readData('_t_co_consts')
    co_consts = _fake_code_tuple(_co_consts)
    # co_consts = TYPE_SMALL_TUPLE.to_bytes(
    # 2, byteorder='big') + (len(eval(_co_consts))).to_bytes(2,
    # byteorder='big') + _co_consts

    _co_names = readData('_t_co_names')
    co_names = _fake_code_tuple(_co_names)
    # co_names = TYPE_SMALL_TUPLE.to_bytes(
    # 2, byteorder='big') + (len(eval(_co_names))).to_bytes(2,
    # byteorder='big') + _co_names

    _co_varnames = readData('_t_co_varnames')
    co_varnames = _fake_code_tuple(_co_varnames)
    # co_varnames = TYPE_SMALL_TUPLE.to_bytes(
    # 2, byteorder='big') + (len(eval(_co_varnames))).to_bytes(2,
    # byteorder='big') + _co_varnames

    _co_freevars = readData('_t_co_freevars')
    co_freevars = _fake_code_tuple(_co_freevars)
    # co_freevars = TYPE_SMALL_TUPLE.to_bytes(
    # 2, byteorder='big') + (len(eval(_co_freevars))).to_bytes(2,
    # byteorder='big') + _co_freevars

    _co_cellvars = readData('_t_co_cellvars')
    co_cellvars = TYPE_REF.to_bytes(
        1, byteorder='big') + (len(eval(_co_cellvars))).to_bytes(1, byteorder='big') + _co_cellvars

    _co_filename = readData('_t_co_filename')
    co_filename = TYPE_SHORT_ASCII.to_bytes(
        1, byteorder='big') + (len(_co_filename)).to_bytes(1, byteorder='big') + _co_filename

    _co_name = readData('_t_co_name')
    co_name = TYPE_SHORT_ASCII.to_bytes(
        1, byteorder='big') + (len(_co_name)).to_bytes(1, byteorder='big') + _co_name

    co_firstlineno = (int(readData('_t_co_firstlineno'))
                      ).to_bytes(4, byteorder='big')

    _co_lnotab = readData('_t_co_lnotab')
    co_lnotab = TYPE_STRING.to_bytes(
        1, byteorder='big') + (len(_co_lnotab)).to_bytes(4, byteorder='big') + _co_lnotab

    return code_type + co_argcount + co_kwonlyargcount + co_nlocals + co_stacksize + co_flags + \
        co_code + co_consts + co_names + co_varnames + co_freevars + co_cellvars + \
        co_filename + co_name + co_firstlineno + co_lnotab


def parse_code(fp):
    code = int.from_bytes(fp.read(1), 'little')
    code_type = code & ~FLAG_REF
    code_flag = code & FLAG_REF

    idx = len(REFS_HASH)
    if code_flag:
        REFS_HASH[idx] = None

    code_dict = {}
    code_obj = b''
    if code_type == TYPE_CODE:
        print("%s code %s" % ("=" * 30, "=" * 30))
        # print('code tell', fp.tell() - 1)
        code_dict['type'] = 'code'
        code_dict['co_argcount'] = int.from_bytes(fp.read(4), 'little')
        # print('co_argcount', code_dict['co_argcount'])
        code_dict['co_kwonlyargcount'] = int.from_bytes(fp.read(4), 'little')
        # print('co_kwonlyargcount', code_dict['co_kwonlyargcount'])
        code_dict['co_nlocals'] = int.from_bytes(fp.read(4), 'little')
        # print('co_nlocals', code_dict['co_nlocals'])
        code_dict['co_stacksize'] = int.from_bytes(fp.read(4), 'little')
        # print('co_stacksize', code_dict['co_stacksize'])
        code_dict['co_flags'] = int.from_bytes(fp.read(4), 'little')
        # print('co_flags', code_dict['co_flags'])
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
        print('code tell end', fp.tell())
    elif code_type == TYPE_STRING:
        print("%s string %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'string'
        length = int.from_bytes(fp.read(4), 'little')
        code_dict['length'] = length
        # todo
        value = fp.read(length)
        code_dict['value'] = str(value)
        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SMALL_TUPLE:
        print("%s tuple %s" % ("=" * 30, "=" * 30))
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
        print("%s long %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'long'
        value = int.from_bytes(fp.read(4), 'little')
        code_dict['value'] = value
        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SHORT_ASCII:
        print("%s TYPE_SHORT_ASCII unicode %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'unicode'
        size = int.from_bytes(fp.read(1), 'little')
        code_dict['size'] = size
        code_dict['value'] = fp.read(size).decode()
        print(code_dict['value'])
        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_SHORT_ASCII_INTERNED:
        print("%s TYPE_SHORT_ASCII_INTERNED unicode %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'unicode'
        size = int.from_bytes(fp.read(1), 'little')
        code_dict['size'] = size
        code_dict['value'] = fp.read(size).decode()
        print(code_dict['value'])
        if code_flag:
            REFS_HASH[idx] = code_dict['value']
    elif code_type == TYPE_REF:
        print("%s ref %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'ref'
        code_dict['ref'] = int.from_bytes(fp.read(4), 'little')
        code_dict['value'] = REFS_HASH[code_dict['ref']]
    elif code_type == TYPE_NONE:
        print("%s none %s" % ("=" * 30, "=" * 30))
        code_dict['type'] = 'none'
    else:
        print(code_type)
    return code_dict


def parse_pyc(file_name):
    pyc_dict = {}
    with open(file_name, 'rb') as fp:
        magic_number = int.from_bytes(fp.read(2), 'little')
        # print(magic_number)
        # if magic_number >= 3390 and magic_number <= 3394:
        #     pyc_dict['version'] = 'Python 3.7'
        # else:
        #     print('only support Python 3.7')
        #     exit(0)
        _ = fp.read(2)
        timestamp = int.from_bytes(fp.read(4), 'little')
        pyc_dict['modified'] = str(datetime.datetime.fromtimestamp(timestamp))
        source_size = int.from_bytes(fp.read(4), 'little')
        pyc_dict['size'] = source_size
        pyc_dict['code'] = parse_code(fp)
    return(pyc_dict)


def main():
    file_name = '_en36.pyc'
    obj = None
    function_start = 52
    function_end = 418
    write_pyc(file_name, function_start, function_end)
    # with open('en36.pyc', 'rb') as fp:
    #     obj = fp.read()
    # print(obj[function_tell:])
    # nobj = obj[:function_tell] + b'' + obj[function_tell:]
    # with open('_en36.pyc', 'wb') as fp:
    #     fp.write(nobj)
    pycObj = parse_pyc(file_name)
    print(json.dumps(pycObj, indent=2))

if __name__ == '__main__':
    main()
    # from xdis.load import check_object_path, load_module
    # xx = {}
    # x = load_module('/Users/virink/tmp/thuctf2018/en36.pyc', xx)
    # print(x)
