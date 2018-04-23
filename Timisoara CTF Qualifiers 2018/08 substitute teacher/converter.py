alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "kufxbhaoiyqtmnezwgscdpljrv"

trans = {}
for i in range(len(key)):
    trans[key[i]] = alphabet[i]

ciphertext = open("ciphertext.txt")
output = open("output.txt", "w")

while True:
    c = ciphertext.read(1)
    if not c: break
    if c in trans: c = trans[c]
    output.write(c)

ciphertext.close()
output.close()