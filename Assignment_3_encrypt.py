def encrypt_permutation(plaintext, order):
    out = ""
    block_size = 5
    for i in range(int(len(plaintext) / block_size)):
        for j in order:
            out += plaintext[i * block_size + j]
    return out


plain = "breaker of this code will be blessed by the squeaky " \
        "spirit residing in the hole. go ahead, and find a way of " \
        "breaking the spell on him cast by the evil"

key = {
    'a': 'q',
    'b': 'j',
    'c': 'e',
    'd': 'p',
    'e': 'v',
    'f': 's',
    'g': 'g',
    'h': 'f',
    'i': 'c',
    'j': 'k',
    'k': 'm',
    'l': 't',
    'm': 'u',
    'n': 'y',
    'o': 'w',
    'p': 'h',
    'q': 'i',
    'r': 'n',
    's': 'l',
    't': 'a',
    'u': 'd',
    'v': 'b',
    'w': 'r',
    'x': 'o',
    'y': 'x',
    'z': 'z'
}

clean_plain = "".join([c for c in plain if c.isalpha()])
print("Plain Text: ", plain)
print("Clean Plain Text: ", clean_plain)
substituted = ""
permuted = encrypt_permutation(clean_plain, [3, 4, 1, 0, 2])
# print(clean_plain[3])

print("Permuted Text: ", permuted)

for ch in permuted.lower():
    substituted += key[ch]

print("Encrypted Text: ", substituted)

