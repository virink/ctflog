import base64

part_1 = 'cmFnZVq'
part_2 = '95b3Vy'
part_3 = 'X2RyZWFt'
part_4 = 'ISEh'


def decode():
    secret = part_1[:-1] + part_2 + part_3 + part_4
    print base64.b64decode(secret)

decode()
