#  import numpy as np
cipher = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc" \
         "xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq" \
         "rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. " \
         "lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf" \
         "avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm" \
         "vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml" \
         "lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf."

plain = "breaker of this code will be blessed by the squeaky " \
        "spirit residing in the hole. go ahead, and find a way of " \
        "breaking the spell on him cast by the evil"
# cipher = "wslaklf ra qcnd xrox hlee wl wellddo wc qul dlvgskb duxaaq xldxoxji qj xcl ercl. " \
#          "ic srlsj, soo fojx shru sf wslakxqi jcl lbdee cj rxp dsnq wc qul lexm yssffa. qdl " \
#          "cbxqxa rf lcq nspl msj sd xehdus hxuc qrv. jxfo qpl csihn xsjc qosq exhe euq lrv qvr " \
#          "rf lcq nsdlm. xq vrheo kspl usv r psnxixsr, jj elqd dcss yjffqa! sr ic qrarciv, dbksl qcs blddarho:"
# password = "kra_esyjw_dv"
# clean_password ="kraesyjwdv"
op = ""
clean_cipher = "".join([c for c in cipher if c.isalpha()])
print("The clean cipher is")
print(clean_cipher)
print("")
print("")

print("The length of the cipher is " + str(len(clean_cipher)))
print("")
print("")

# key = {
#     'a': 'r',
#     'b': 'p',
#     'c': 'h',
#     'd': 's',
#     'e': 'l',
#     'f': 'f',
#     'g': 'q',
#     'h': 'w',
#     'i': 'g',
#     'j': 'n',
#     'k': 'k',
#     'l': 'e',
#     'm': 'v',
#     'n': 'c',
#     'o': 'd',
#     'p': 'm',
#     'q': 't',
#     'r': 'o',
#     's': 'a',
#     't': '?',
#     'u': 'y',
#     'v': 'u',
#     'w': 'b',
#     'x': 'i',
#     'y': '?',
#     'z': 'z'
# }

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

tmp = ""
for ch in clean_cipher.lower():
    tmp += key[ch]

print(tmp)
print("")
print("")
print("")

out = ""
block_size = 5
for i in range(int(len(tmp) / block_size)):
    out += tmp[i * block_size + 3]
    out += tmp[i * block_size + 2]
    out += tmp[i * block_size]
    # print(out)
    # print(out)
    out += tmp[i * block_size + 1]
    out += tmp[i * block_size + 4]

print(out)
