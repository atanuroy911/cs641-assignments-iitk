import time
from tqdm import tqdm

import paramiko

hostname = "172.27.26.188"
port = 22
username = "student"
password = "cs641"

ssh = paramiko.client.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password, allow_agent=False, look_for_keys=False)
print('Successfully connected to %s' % hostname)

remote_conn = ssh.invoke_shell()
output = remote_conn.recv(1000)

time.sleep(2)
# Clearing output.
if remote_conn.recv_ready():
    output = remote_conn.recv(1000)

# Insert Team
remote_conn.send(b'dark_army\n')
time.sleep(1)
# Getting output I want.
if remote_conn.recv_ready():
    output = remote_conn.recv(100)
print(output.decode('utf-8'))

# Insert Password

remote_conn.send(b'army7890\n')
remote_conn.send(b'\n')
time.sleep(1)
if remote_conn.recv_ready():
    output = remote_conn.recv(5000)
print(output.decode('utf-8'))

# Set Level

remote_conn.send(b'4\n')
time.sleep(1)
if remote_conn.recv_ready():
    output = remote_conn.recv(5000)
print(output.decode('utf-8'))

# Send 'read' command

remote_conn.send(b'read\n')
time.sleep(1)
if remote_conn.recv_ready():
    output = remote_conn.recv(5000)
print(output.decode('utf-8'))

# Send Inputs

f = open('input3.txt')
f2 = open('response3.txt', 'w+')
Lines = f.readlines()
# out = []
count = len(Lines)
with tqdm(total=count) as pbar:
    for line in Lines:
        line = line.split(',')[0]
        print(line)
        remote_conn.send(bytes(line, encoding="utf-8") + b'\n')
        time.sleep(1)
        if remote_conn.recv_ready():
            output = remote_conn.recv(5000)
            x = output[-43:-27]
            # print(output.decode('utf-8'))
            # out.append(x)
            x = x.decode('utf-8')
            # print(str(x))
            f2.write(x)
            f2.write('\n')
            f2.flush()
            pbar.update(1)
f2.close()

