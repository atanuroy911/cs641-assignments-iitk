# import sys
# import time
# from tqdm import tqdm
#
# import paramiko
#
# hostname = "172.27.26.188"
# port = 22
# username = "student"
# password = "cs641"
#
# ssh = paramiko.client.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname, port, username, password, allow_agent=False, look_for_keys=False)
# print('Successfully connected to %s' % hostname)
#
# remote_conn = ssh.invoke_shell()
# output = remote_conn.recv(1000)
#
# time.sleep(2)
# # Clearing output.
# if remote_conn.recv_ready():
#     output = remote_conn.recv(1000)
#
# # Insert Team
# remote_conn.send(b'dark_army\n')
# time.sleep(1)
# # Getting output I want.
# if remote_conn.recv_ready():
#     output = remote_conn.recv(100)
# print(output.decode('utf-8'))
#
# # Insert Password
#
# remote_conn.send(b'army7890\n')
# remote_conn.send(b'\n')
# time.sleep(1)
# if remote_conn.recv_ready():
#     output = remote_conn.recv(5000)
# print(output.decode('utf-8'))
#
# # Set Level
#
# remote_conn.send(b'4\n')
# time.sleep(1)
# if remote_conn.recv_ready():
#     output = remote_conn.recv(5000)
# print(output.decode('utf-8'))
#
# # Send 'read' command
#
# remote_conn.send(b'read\n')
# time.sleep(1)
# if remote_conn.recv_ready():
#     output = remote_conn.recv(5000)
# print(output.decode('utf-8'))


# def getcipher(text):
#   defbody['plaintext'] = text
#   resp = r.post(url, json=defbody, verify=False)
#   return resp.json()['ciphertext']

# if userinput:
#   while True:
#     text = input()
#     print(text + ': ' + getcipher(text))
#     sys.stdout.flush()
# else:
# text = 'c'*1000
# alphas = list(string.ascii_lowercase)
# alphas.extend(list(string.ascii_uppercase))
# alphas.extend(list(range(10)))
text = []
b_dict = {
    'f': '0000',
    'g': '0001',
    'h': '0010',
    'i': '0011',
    'j': '0100',
    'k': '0101',
    'l': '0110',
    'm': '0111',
    'n': '1000',
    'o': '1001',
    'p': '1010',
    'q': '1011',
    'r': '1100',
    's': '1101',
    't': '1110',
    'u': '1111'
}
with open("input.txt", "r") as myfile:
    text = myfile.readlines()
with open("random_binary.txt", "w") as fw:
    for lines in text:
        cipher = lines[0:16]
        print(cipher)
        for i in range(0, 16):
            fw.write(b_dict[cipher[i]])
            # print(b_dict[cipher[i]])
        fw.write("\n")
    #   di.setdefault(cipher, [])
    #   di[cipher].append(plaintext)

# for key in di:
#     print(key + ': ')
#     print(di[key])
#
#
# # Send Inputs
#
# f = open('input.txt')
# f2 = open('response.txt', 'w+')
# Lines = f.readlines()
# # out = []
# count = len(Lines)
# with tqdm(total=count) as pbar:
#     for line in Lines:
#         line = line.split(',')[0]
#         print(line)
#         remote_conn.send(bytes(line, encoding="utf-8") + b'\n')
#         time.sleep(0.5)
#         if remote_conn.recv_ready():
#             output = remote_conn.recv(5000)
#             x = output[-43:-27]
#             # print(output.decode('utf-8'))
#             # out.append(x)
#             x = x.decode('utf-8')
#             # print(str(x))
#             f2.write(x)
#             f2.write('\n')
#             f2.flush()
#             pbar.update(1)
# f2.close()
