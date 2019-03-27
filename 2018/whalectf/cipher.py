import string

cipher = "wDhlpGvy{raJz_cmIL_dUvq_XJ}"

flag = "whaleCTF{0000_0000_00T0_00}"

# A-Z 65-90
# a-z 97-122

# w -> w
# D -> h
# h -> a
# l -> l
# p -> e
# G -> C
# v -> T
# y -> F

# a = a + 7
# b = b + 8
# c = c + 9
# d = d + 10
# e = e + 11
# f = f + 12
# g = g + 13
# h = 14
# i 15
# j 16
# k 17
# l 18
# m
# n
table = '_________1_________2______' + '___3_________4_________5__'
table = '12345678901234567890123456' + '78901234567890123456789012'
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'
table = '___h__C___________________' + '789012345678901e_____Tw_F_'
table = '___h__C___________________' + '0123456789012345678901w_F_'
table = '___h__C___________________' + '_______a___l___e_____Tw_F_'
table = '___h__C___________________' + '_______a___l___e_____Tw_F_'
# table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'

t2 = {table[n]: n for n in range(len(table))}

for i in range(8):
    c = cipher[i]
    f = flag[i]
    # print("%s -> %s" % (c, f))
    print("%s -> %s\t%d\t%d\t%d\t%d" %
          (c, f, ord(c), ord(f), ord(c) - ord(f), t2[c] - t2[f]))
