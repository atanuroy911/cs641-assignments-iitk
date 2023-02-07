def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return "".join(encrypt_text)


def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


if __name__ == "__main__":
    string = input("Enter the Encrypted Message: ").upper().replace(" ", "").replace(",", "").replace(".", "")
    keyword = input("Enter the keyword: ").upper()
    key = generateKey(string, keyword)
    # encrypt_text = encryption(string, key)
    print("Encrypted message:", string)
    print("Decrypted message:", decryption(string, key))

# Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg.
# 	Urfjm xwy yjg rbbufqwi "vjg_djxn_ofs_dg_rmncbgi" yq iq uqtxwlm.
# 	Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv,
# 	aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.
