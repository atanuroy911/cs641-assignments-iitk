from des import *
import itertools
import sys
import os
import string
import random
import numpy as np

input_set = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']

# input xor required for 1st trial 0000801000004000
left_xor = ['0000', '0000', '0000', '0000', '1000', '0000', '0001', '0000']  # 00008010
right_xor = ['0000', '0000', '0000', '0000', '0100', '0000', '0000', '0000']  # 00004000

# input xor required for 2nd trail


bit_set = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
           '1101', '1110', '1111']
alphabet_map = {}


def create_alphabet_map(start):
    global alphabet_map
    k = start
    for i in input_set:
        alphabet_map[i] = bit_set[k]
        k = (k + 1) % 16


def findPair(inp, xor_list):
    tmp_list = list(inp)
    plaintext2 = []
    k = 0
    for i in tmp_list:
        t1 = list(alphabet_map[i])
        t2 = list(xor_list[k])
        xor_result = xor(t1, t2)
        for j in alphabet_map:
            if alphabet_map[j] == (''.join(xor_result)):
                plaintext2.append(j)
                break
        k += 1
    plaintext2 = ''.join(plaintext2)
    return plaintext2


# Returns the plaintext for the entered plaintext maintaining xor difference
# inp will be in the form - "16 chars : {L_0R_0}"
def generate_pair(inp):
    L_10 = inp[:8]
    R_10 = inp[8:]
    L_20 = findPair(L_10, left_xor)
    R_20 = findPair(R_10, right_xor)
    return L_20 + R_20


def gen_random_str(character_set, size):
    random_str = ''
    for i in range(size):
        character = random.choice(character_set)
        random_str += character
    return random_str


def input_pairs():
    Diff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Bin_Inp = []
    for i in range(10000):
        tmp = '{:0>64}'.format(format(i, "b"))
        tmp = [int(tmp[j]) for j in range(64)]
        Bin_Inp.append(tmp)
        Bin_Inp.append(list(np.bitwise_xor(tmp, Diff)))

    mapping = {}
    for i in range(16):
        num = '{:0>4}'.format(format(i, "b"))
        numi = int(num[3]) + 2 * int(num[2]) + int(num[1]) * 4 + int(num[0]) * 8
        mapping[num] = chr(ord('f') + numi)
    mapping

    Str_inp = []
    for i in range(len(Bin_Inp)):
        string = ""
        for j in range(16):
            tmp = str(Bin_Inp[i][j * 4:(j * 4) + 4][0]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][1]) + str(
                Bin_Inp[i][j * 4:(j * 4) + 4][2]) + str(Bin_Inp[i][j * 4:(j * 4) + 4][3])
            string = string + mapping[tmp]
        Str_inp.append(string)
    if os.path.isfile('input2.txt'):
        os.remove('input2.txt')

    # f = open('input.txt', 'w+')
    # count = 0
    # while count < 500:
    #     plaintext1 = gen_random_str(input_set, 16)
    #     f.write(plaintext1 + ",\n")
    #     plaintext2 = generate_pair(plaintext1)
    #     f.write(plaintext2 + ",\n")
    #     count += 1
    # f.close()

    file = open("input2.txt", "w")
    for i in Str_inp:
        file.write(i)
        file.write(",\n")
    file.close()

def convert_responsefile_to_cipher():
    if os.path.isfile('response2.txt'):
        f1 = open('response2.txt', 'r')
        f2 = open('cipherpair2.txt', 'w+')
        flag = 0
        for line in f1:
            if flag == 0:
                f2.write(line[:16])
                flag = 1
            else:
                f2.write(' ' + line[:16] + '\n')
                flag = 0
        f1.close()
        f2.close()
    else:
        print("No Responsefile.txt found")
        raise SystemExit


def get_diff_of_cipherpair(left, right):
    left_bitarr = list(left)
    right_bitarr = list(right)
    diff_bitarr = xor(left_bitarr, right_bitarr)
    return ''.join(diff_bitarr)


# convert text pairs to bit strings - save them in outputplain.txt/outputcipher.txt
def convert_pairs_to_bitstring(flag):
    if flag == 'c':
        if os.path.isfile('cipherpair2.txt'):
            f1 = open('cipherpair2.txt', 'r')
            f2 = open('cipher2.txt', 'w+')
        else:
            print("No input file cipherpair.txt found")
            raise SystemExit
    for line in f1:
        pair_first = line[:16]
        pair_second = line[17:-1]
        input1 = [alphabet_map[ch] for ch in pair_first]
        input2 = [alphabet_map[ch] for ch in pair_second]
        bit_string1 = ''.join(input1)
        bit_string2 = ''.join(input2)
        f2.write(bit_string1 + ' ' + bit_string2 + '\n')
    f1.close()
    f2.close()


create_alphabet_map(0)

# --------------Order to run -------------------#

# PHASE 1
# Uncomment the following code to run Phase 1 - generate input pairs
# input_pairs()

# PHASE 2 - Run Response.py to get ciphertexts of the input pairs

# PHASE 3 - Uncomment the following lines
# convert_responsefile_to_cipher()
# convert_pairs_to_bitstring('c')

# PHASE 4 - compute the input output xors into the sboxes in the last round
# Run compute_input_output_xor.py in order to do this

# PHASE 5 - Find key possibilities by running find_key.py
