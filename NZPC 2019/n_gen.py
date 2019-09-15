from sys import stdout
from random import Random

r = Random()

N = r.randrange(2, 100)
Q = r.randrange(1, 100)

print(f"{N} {Q}")
for i in range(N):
	stdout.write(str(r.randrange(0, N)) + " ")
stdout.write("\n")
for i in range(Q):
	A = 1
	B = 1
	while A == B:
		A = r.randrange(0, N)
		B = r.randrange(0, N)
	print(f"{A} {B}")
