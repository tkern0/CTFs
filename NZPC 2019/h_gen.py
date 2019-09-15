from sys import stdout
from random import Random

r = Random()

print("A")
print(f"09 11 {r.randrange(0,24)}:{r.randrange(0,60)}")
offset = r.randrange(-14, 14)
if offset == 0:
	print("00:00")
else:
	print(f"{'+' if offset > 0 else ''}{offset}:{r.randrange(0,60)}")
print("B")
offset = r.randrange(-14, 14)
if offset == 0:
	print("00:00")
else:
	print(f"{'+' if offset > 0 else ''}{offset}:{r.randrange(0,60)}")
print(f"{r.randrange(0,10)}:{r.randrange(0,60)}")
