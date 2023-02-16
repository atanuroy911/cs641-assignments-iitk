import string


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


def alphabet_permutation(num):
    import itertools
    alphabet = string.ascii_lowercase
    s = alphabet[:num]
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    return permutations


def keygen(num):
    combinations = alphabet_permutation(num)
    alphabet = list(string.ascii_lowercase)
    new_alphabet = []
    keylist = []
    for i in range(len(combinations)):
        # print(i)
        for j in range(num):
            new_alphabet.append(alphabet[j])
        key = dict(zip(new_alphabet, combinations[i]))
        keylist.append(key)

    return keylist


cipher = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc"
#          "xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq" \
#          "rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. " \
#          "lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf" \
#          "avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm" \
#          "vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml" \
#          "lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf."

## DRIVER CODE

data = list('01234')
for p in permutation(data):
    print(p)

print(alphabet_permutation(3))
print(keygen(3))

clean_cipher = "".join([c for c in cipher if c.isalpha()])
print("Clean Cipher: ", clean_cipher)

substituted = ""


## Original Dictionary Attack

with open('data.txt', 'w') as f:
    for p in permutation(data):
        permuted = decrypt_permutation(clean_cipher, p)
        f.write(f"Trying Permutation: {p}\n")
        for k in keygen(10):
            substituted = ""
            # print(f"Trying Permutation: {p}\n")
            # print(f"Trying Key: {k}\n")
            f.write(f"Trying Permutation: {p}\n")
            f.write(f"Trying Key: {k}\n")
            for ch in permuted.lower():
                try:
                    substituted += k[ch]
                except:
                    substituted += ch
            f.write(f"Substituted Text: {substituted}\n")
