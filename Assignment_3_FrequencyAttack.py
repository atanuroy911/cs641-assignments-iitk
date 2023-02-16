# decrypt = "etaoinsrhldcumfpgwybvkxjqz"  # Plain
# encrypt = "vapgwhasfkuinjtervxobcqldy"  # Cipher

decrypt = "abcdefghijklmnopqrstuvwxyz"
encrypt = "qjepvsgfckmtuywhinladbroyz"

def decrypt_permutation(ciphertext, order):
    out = ""
    block_size = 5
    for i in range(int(len(ciphertext) / block_size)):
        for j in order:
            out += ciphertext[i * block_size + int(j)]
    return out


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


cipher = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc" \
         "xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq" \
         "rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. " \
         "lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf" \
         "avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm" \
         "vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml" \
         "lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf."


# Driver code
data = list('01234')

clean_cipher = "".join([c for c in cipher if c.isalpha()])
print("Clean Cipher: ", clean_cipher)

cipher_length = len(clean_cipher)

counter = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    n = clean_cipher.count(i) * 100 / cipher_length
    counter[i] = n
counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(counter)

with open('data.txt', 'w') as f:
    for p in permutation(data):
        # p = [3, 2, 4, 0, 1]
        permuted = decrypt_permutation(clean_cipher, p)
        print(permuted)
        # print('breakerofthiscodewillbeblessedbythesquea')
        f.write(f"Trying Permutation: {p}\n")
        f.write(f"Permuted Text: {permuted}\n")
        txt = list(permuted)

        for i in range(len(txt)):
            if not txt[i].isalpha():
                continue
            try:
                n = encrypt.index(txt[i])
                txt[i] = decrypt[n]
            except:
                continue
        txt = "".join(txt)
        f.write(f"Changed Text: {txt}\n")
        print(txt)
