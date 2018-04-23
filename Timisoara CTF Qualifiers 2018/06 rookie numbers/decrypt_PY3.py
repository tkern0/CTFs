import re
import rsa

with open("params.txt") as f:
    for l in f:
        if l[0] == "n":
            n = int(l.split()[1])
        elif l[0] == "c":
            c = int(l.split()[1])

with open("key_info.txt") as f:
    match = re.search(r"privateExponent:([\s:0-9a-f]*)", f.read(), flags=re.I)
    d = int(re.sub(r"[\s:]", "", match.group(1)), 16)

m = rsa.core.decrypt_int(c, d, n)

m_hex = str(hex(m))[2:]
output = ""
for i in range(0, len(m_hex), 2):
    val = int(m_hex[i:i+2], 16)
    output += chr(val)
print(output)