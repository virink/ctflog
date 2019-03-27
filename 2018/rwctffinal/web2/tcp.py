import socket
import struct


c = []
with open('tcp', 'r') as f:
    c = f.readlines()
# print(c[:10])


def clearSpace(d):
    return d.replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")


def h2ip(data):
    return socket.inet_ntoa(struct.pack("!I", socket.ntohl(int(data.upper(), 16))))


def h2port(data):
    return int(data.upper(), 16)


def address2ipport(data):
    _data = data.split(":")
    # print(_data)
    return "%s:%d" % (h2ip(_data[0]), h2port(_data[1]))


def a(data):
    if data[0] == '':
        data = data[1:]
    local_address = address2ipport(data[1])
    rem_address = address2ipport(data[2])
    return "%s\t%s\r\n" % (local_address, rem_address)


def test():
    r = clearSpace(c[2])
    print(r)


def do():
    with open("_tcp", "w") as f:
        f.write("local_address\trem_address\r\n")
        for i in c[1:-1]:
            try:
                f.write(a(clearSpace(i)))
            except Exception as e:
                print(e)
                print(clearSpace(i))


if __name__ == '__main__':
    # test()
    do()
