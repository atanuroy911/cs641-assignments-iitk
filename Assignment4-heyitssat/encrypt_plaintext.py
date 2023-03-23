import requests as Requests
import json as JSON
import sys

url = "http://172.27.26.132:9999/des"

payload = "\"plaintext\":\"{0}\",\"teamname\":\"Rijndael\"," +\
        "\"password\":\"af69610407ebc949b3033c6cbcea3438\""
headers = {'host': "172.27.26.132:9999"}

bits_reverse = {
        'f':'f',
        'g':'h',
        'h':'g',
        'i':'i',
        'j':'n',
        'k':'p',
        'l':'o',
        'm':'q',
        'n':'j',
        'o':'l',
        'p':'k',
        'q':'m',
        'r':'r',
        's':'t',
        't':'s',
        'u':'u',
        }

def encrypt(msg, rev_bits=True):
    data = "{" + payload.format(str(msg)) + "}"
    req_headers = dict(headers)
    req_headers["content-length"] = str(len(data))
    resp = Requests.post(url, data=data, headers=req_headers)
    #  print(resp.text)
    if rev_bits:
        return "".join([bits_reverse[c] for c in JSON.loads(resp.text)["ciphertext"]])
    else:
        return JSON.loads(resp.text)["ciphertext"]

def encrypt_file(f1, f2):
    with open(f1, 'r') as plain_file, open(f2, 'w') as cipher_file:
        for lines in plain_file.readlines():
            inps = lines.split()
            #  print(inps)
            outs = [encrypt(msg, rev_bits=False) for msg in inps]
            #  print(outs)
            cipher_file.write(" ".join(outs) + "\n")

if len(sys.argv) < 3:
    print("python <.pyfile> <input_file> <output_file>")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encrypt_file(input_file, output_file)
    print("The file: {} has been encrypted to {}".format(input_file, output_file))
