import os
p, q = open("factors.txt").read().split("\n")
os.system("python rsatool.py -f PEM -o key.pem -p {} -q {}".format(p, q))
os.system("openssl rsa -noout -text -in key.pem > key_info.txt")