import tarfile
import sys
import uuid
import os


def untar(filename):
    os.chdir('/tmp/pwnhub/')
    t = tarfile.open(filename, 'r')
    for i in t.getnames():
        if '..' in i or '.cfg' != os.path.splitext(i)[1]:
            return 'error'
        else:
            try:
                t.extract(i, '/tmp/pwnhub/')
            except Exception, e:
                return e
            else:
                cfgName = str(uuid.uuid1()) + '.cfg'
                os.rename(i, cfgName)
                return cfgName

if __name__ == '__main__':
    filename = sys.argv[1]
    if not tarfile.is_tarfile(filename):
        exit('error')
    else:
        print untar(filename)
