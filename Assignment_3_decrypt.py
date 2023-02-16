def decrypt_permutation(ciphertext, order):
    out = ""
    block_size = 5
    for i in range(int(len(ciphertext) / block_size)):
        for j in order:
            out += ciphertext[i * block_size + j]
    return out


cipher = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc" \
         "xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq" \
         "rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. " \
         "lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf" \
         "avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm" \
         "vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml" \
         "lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf."

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

inv_key = {v: k for k, v in key.items()}

clean_cipher = "".join([c for c in cipher if c.isalpha()])
print("Clean Cipher: ", clean_cipher)
substituted = ""
permuted = decrypt_permutation(clean_cipher, [3, 2, 4, 0, 1])
# print(clean_plain[3])

print("Permuted Cipher: ", permuted)

for ch in permuted.lower():
    substituted += inv_key[ch]

print("Substituted Text: ", substituted)




