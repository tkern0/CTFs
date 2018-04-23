import socket
import sys

ADDRESS = "89.38.210.129"
PORT = 6665

STR_1 = ""
STR_2 = "\x00"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))

command = b" ".join(sys.argv[1:])
s.sendall(b"{}\n{}\n".format(STR_1, STR_2))
s.shutdown(socket.SHUT_WR)
while True:
    data = s.recv(4096)
    if not data:
        break
    print(data)
s.close()
