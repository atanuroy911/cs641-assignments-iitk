import random
import numpy as np
import math


def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


ciphertext = "iogrspjnkjpnihhjjkisnhsptnftfnlo"
print("Length of ciphertext: ", len(ciphertext))
print("Ciphertext (Binary): ", toBinary(ciphertext))


# Diff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Bin_Inp = []
# for i in range(100000):
#     tmp = '{:0>64}'.format(format(i, "b"))
#     tmp = [int(tmp[j]) for j in range(64)]
#     Bin_Inp.append(tmp)
#     Bin_Inp.append(list(np.bitwise_xor(tmp, Diff)))
#
# mapping = {}
# for i in range(16):
#     num = '{:0>4}'.format(format(i, "b"))
#     numi = int(num[3]) + 2 * int(num[2]) + int(num[1]) * 4 + int(num[0]) * 8
#     mapping[num] = chr(ord('f') + numi)
# print(mapping)
#
# Str_inp = []
# for i in range(len(Bin_Inp)):
#     string = ""
#     for j in range(16):
#         tmp = str(Bin_Inp[i][j * 4:(j * 4) + 4][0]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][1]) + str(
#             Bin_Inp[i][j * 4:(j * 4) + 4][2]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][3])
#         string = string + mapping[tmp]
#     Str_inp.append(string)
#
# len(Str_inp)
# print(Str_inp[3])
#
# file = open("inputs.txt", "w")
# for i in Str_inp:
#     file.write(i)
#     file.write("\n")
# file.close()
