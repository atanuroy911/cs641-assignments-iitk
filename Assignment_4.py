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

diff_char = "405c000004000000"

init_perm = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

inv_init_perm = []
for i in range(1, 65):
    inv_init_perm.append(init_perm.index(i) + 1)


# print(inv_init_perm)

def hex2bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


def bin2hex(bin_string):
    return hex(int(bin_string, 2))[2:].upper()


char_seq = hex2bin(diff_char)
diff = ''
for i in inv_init_perm:
    diff += char_seq[i - 1]
print("Difference Found: ", diff)
print("Difference Found (HEX): ", bin2hex(diff))

list_diff = [int(char) for char in diff]
print(list_diff)
Bin_Inp = []
for i in range(100000):
    tmp = '{:0>64}'.format(format(i, "b"))
    tmp = [int(tmp[j]) for j in range(64)]
    Bin_Inp.append(tmp)
    Bin_Inp.append(list(np.bitwise_xor(tmp, list_diff)))

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i, "b"))
    numi = int(num[3]) + 2 * int(num[2]) + int(num[1]) * 4 + int(num[0]) * 8
    mapping[num] = chr(ord('f') + numi)
print(mapping)

Str_inp = []
for i in range(len(Bin_Inp)):
    string = ""
    for j in range(16):
        tmp = str(Bin_Inp[i][j * 4:(j * 4) + 4][0]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][1]) + str(
            Bin_Inp[i][j * 4:(j * 4) + 4][2]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][3])
        string = string + mapping[tmp]
    Str_inp.append(string)

len(Str_inp)
print(Str_inp[3])

file = open("inputs.txt", "w")
for i in Str_inp:
    file.write(i)
    file.write("\n")
file.close()
