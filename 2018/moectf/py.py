# import base64
# r = open('flag', 'r')


# rflag = 'bX;oY4Tpe4D8Q2;VRW:{U2;IQIP8fR?@'
# key = base64.b64encode(r.read())


# flag = ''
# for i in range(len(key) / 4):
#     for j in range(4):
#         flag += chr(ord(key[i * 4 + j]) + j)

# if rflag == flag:
#     print('You are right.')


rflag = 'bX;oY4Tpe4D8Q2;VRW:{U2;IQIP8fR?@'
flag = ''
for i in range(8):
    for j in range(4):
        flag += chr(ord(rflag[i * 4 - j]) - j)
print(flag)
