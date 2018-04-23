import numpy as np
import re

def int_to_str(n):
    return bytearray.fromhex(hex(n)[2:]).decode()

# Get coords from input file
# I reformatted it to be more readable first, this would break on the default file
chunks = [set(), set(), set(), set()]
chunk_num = 0
with open("shares.txt") as f:
    for line in f:
        m = re.search(r"'chunk_(\d)'", line, flags=re.I)
        if m:
            chunk_num = int(m.group(1))
        m = re.search(r"'y': (\d*?),\s*?'x': (\d*?)\s", line, flags=re.I)
        if m:
            chunks[chunk_num].add((int(m.group(2)), int(m.group(1))))

# Try fill in all the missing coords
for c1 in range(4):
    for c2 in range(c1 + 1, 4):
        # Find the offset between the two chunks
        offset = None
        for i in chunks[c1]:
            for j in chunks[c2]:
                if i[0] == j[0]:
                    offset = i[1] - j[1]
            if not offset == None:
                break
        print("Offset between chunk_{} and chunk_{} is: {}".format(c1, c2, hex(offset)))
        # Use the offset to work out missing coords
        for i in chunks[c1]:
            new_coords = (i[0], i[1] - offset)
            chunks[c2].add(new_coords)
        for i in chunks[c2]:
            new_coords = (i[0], i[1] + offset)
            chunks[c1].add(new_coords)

print("Found all missing coords")

for i in chunks:
    print(sorted(list(i))[:13])

"""
This gives rubbish like starting bytes > 7f or endings with 5 nulls in a row

# Because all coefficients are equal we only need to do this once
x_matrix = []
y_matrix = []
for row in sorted(list(chunks[0]))[:13]:
    x, y = row[0], row[1]
    x_matrix.append([x**i for i in range(0, 13)])
    y_matrix.append([y])
a = np.matrix(x_matrix)
b = np.array(y_matrix)
c = np.linalg.inv(a)
d = c*b
print(d)
print(hex(int(d[0])))
"""

"""
let's try manually
timctf{????????????????????????????????}
                 t  i  m  c  t  f  {  ?  ?  ?
chunk_0:        74 69 6d 53 74 66 7b ?? ?? ??
offset 0, 1:  - 26 19 f9 04 22 33 11 f5 da 2c
---------------------1-----------------------
chunk_1:        4e 49 74 4f 52 33 6a ?? ?? ??
                 N  I  t  O  R  3  j  ?  ?  ?
        might lose having to carry ^

                 t  i  m  c  t  f  {  ?  ?  ?
chunk_0:        74 69 6d 53 74 66 7b ?? ?? ??
offset 0, 2:  - 06 15 0e 20 02 0d 0a f0 00 00
---------------------------------------------
chunk_2:        6e 54 5f 33 72 59 71 ?? ?? ??
                 n  T  _  3  r  Y  q  ?  ?  ?

                 t  i  m  c  t  f  {  ?  ?  ?
chunk_0:        74 69 6d 53 74 66 7b ?? ?? ??
offset 0, 3:  - 74 69 6d 13 08 33 46 f0 ea e2
---------------------------------------------
chunk_3:        00 00 00 40 6c 33 35 ?? ?? ??
                          @  l  3  5  ?  ?  ?
        might lose having to carry ^

=============================================

                 N  I  t  O  R  3  j  ?  ?  ?
chunk_1:        4e 49 74 4f 52 33 6a ?? ?? ??
offset 1, 2:  + 20 04 ea e1 20 26 07 05 da 2c
---------------------1--1--------------------
chunk_2:        6e 4e 5f 30 72 59 71 ?? ?? ??
                 n  N  _  0  r  Y  q  ?  ?  ?
                    ^ wtf ^        ^
  this is consistent so char 8 has ^
         to be >f5 ????

                 N  I  t  O  R  3  j  ?  ?  ?
chunk_1:        4e 49 74 4f 52 33 6a ?? ?? ??
offset 1, 3:  - 4e 4f 74 0e e6 00 34 fb 10 b6
---------------------------1-----------------
chunk_3:        ff fa 00 40 6c 33 36 ?? ?? ??
                          @  l  3  6
                is it not <fb ???? ^
=============================================

                 n  T  _  3  r  Y  q  ?  ?  ?
chunk_2:        6e 54 5f 33 72 59 71 ?? ?? ??
offset 2, 3:  - 6e 54 5e f3 06 26 3c 00 ea e2
------------------------1--------------------
chunk_3:        00 00 00 40 6c 33 35 ?? ?? ??
                          @  l  3  5  ?  ?  ?
=============================================
                      new assumptions v  v  v
                          @  l  3  5  }  }  }
chunk_3:        00 00 00 40 6c 33 35 7d 7d 7d
offset 3, 0:  + 74 69 6d 13 08 33 46 d0 ea e2
------------------------------------1--1--1--
chunk_1:        74 69 6d 53 74 66 7b 4d 67 5f
                 t  i  m  c  t  f  {  M  g  _
                          seems most likely ^
=============================================

timctf{???NItOR3j???nT_3rYq???   @135??}
          _cant? ^^^^^

           NItOR 3  j  _  c  a  C  A  ?  4
chunk_1:        33 6a f5 63 61 43 41 ?? 34
offset 0, 1:  + 33 11 f5 da 2c da 2c da 2c
---------------------1--1-----1--------------
chunk_0:        59 7c ef 3d 8e 1d 6d ?? 60
           timct f  |    =         m     `
"""
