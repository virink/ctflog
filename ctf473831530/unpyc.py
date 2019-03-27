import marshal
import dis
import struct
from xdis.load import load_module, check_object_path


class PyCodeObject(object):

    def __init__(self):
        self.test = 1


class PyObject(object):

    def __init__(self):
        self.test = 1


def read_pyc(filename):
    filename = check_object_path(filename)
    code_objects = {}
    (version, timestamp, magic_int, co, is_pypy,
     source_size) = load_module(filename, code_objects)
    print(version)
    print(timestamp)
    code_obj(co)


def code_obj(co):
    xco = {i: co.__getattribute__(i)
           for i in dir(co) if i.startswith('co_') and i not in ['co_lnotab'] and co.__getattribute__(i)}  # 'co_code',
    for i in xco:
        print("%s : %s" % (i, xco[i]))
    dis.dis(co)
    print('=' * 30)
    subCo = [i for i in co.co_consts if type(i) == type(co)]
    for i in subCo:
        code_obj(i)


def main():
    read_pyc('crypt.pyc')

if __name__ == '__main__':
    main()
