mapping = ['c','p','t','h','a','w','m','q','b','v','$','r','n','y','$','e','l','s','f','$','$','g','o','i','u','d']
alphabets = [chr(i+ord('a')) for i in range(26)]
print(alphabets)
print(mapping)

print(len(mapping))
key = [(c[0],c[1]) for c in zip(alphabets, mapping)]
for k in key:
    print(str(k[0])+":="+str(k[1]))
print(key)

plain = "Mewa wa mey twsam iepjoys gt mey ipbya. " \
    "Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. " \
    "Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! " \
    "Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh " \
    "iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya.  " \
    "Mey fpaavgsu wa mxSrN03uwdd vwmegnm mey dngmya."
plain = [ c for c in list(plain.lower())]

ans = ""
for c in list(plain):
    if ord(c)<=ord('z') and ord(c)>=ord('a'):
        c = mapping[ord(c)-ord('a')]
    ans += c;

print(''.join(ans))

plain = "fqEo42Bkvt"



ans = ""
ans1 = ""
for c in list(plain):
    if ord(c)<=ord('z') and ord(c)>=ord('a'):
        c = mapping[ord(c)-ord('a')]
    if ord(c)<=ord('Z') and ord(c)>=ord('A'):
        c = chr(ord(mapping[ord(c)-ord('A')]) - ord('a')+ord('A'))
    ans1 += c;
    c = chr(ord(c)-4)
    ans += c;

print(ans1)
#  print(ans)