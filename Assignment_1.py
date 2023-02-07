import string

txt = "Mewa wa mey twsam iepjoys gt mey ipbya. " \
      "Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. " \
      "Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! " \
      "Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh " \
      "vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu " \
      "wa mxSrN03uwdd vwmegnm mey dngmya"
cleaned_txt = txt

for i in string.punctuation:
    cleaned_txt = cleaned_txt.replace(i, "")
cleaned_txt = cleaned_txt.replace(" ", "")
digits = str.maketrans('', '', string.digits)
cleaned_txt = cleaned_txt.translate(digits)
cleaned_txt = cleaned_txt.lower()

txt_len = len(cleaned_txt)

# This section finds the frequency of letters
counter = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    n = cleaned_txt.count(i) * 100 / txt_len
    counter[i] = n
counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(counter)

# Encryption letter list is found through the frequency analysis and trial and error method
# Decryption letter list is from the internet as to which is the most prominent letters used in english language

# ETAOINSRHLDCUMFPGWYBVKXJQZ
# http://pi.math.cornell.edu/~morris/135/letfreq.html

decrypt = "etaoinsrhldcumfpgwybvkxjqz" + "etaoinsrhldcumfpgwybvkxjqz".upper()
encrypt = "ympgwhasekuinjtfrvxobcqldz" + "ympgwhasekuinjtfrvxobcqldz".upper()

print("The given encrypted message is:\n", txt)
print("\n")

txt = list(txt)

for i in range(len(txt)):
    if not txt[i].isalpha():
        continue
    n = encrypt.index(txt[i])
    txt[i] = decrypt[n]
txt = "".join(txt)
b = txt.replace(" ", "")
b = b.replace("\n", "")
print("The decrypted message is:\n", txt)
