from sys import stdin

name1 = stdin.readline()[:-1]
name2 = stdin.readline()[:-1]
s1, s2 = stdin.readline().split(" ")
s1 = int(s1)
s2 = int(s2)

chars = int(stdin.readline())
line = stdin.readline()

t1_turn = True
next_c = False
for char in line:
	if char == "M":
		t1_turn = not t1_turn
	# Turns out this didn't matter - the input data was always valid, we didn't have to perform
	#  verification
	elif char == "R":
		next_c = True
	elif char == "C":
		next_c = False
	elif char == "H":
		if t1_turn:
			s1 += 1
		else:
			s2 += 1
	elif char == "P":
		if t1_turn:
			s1 += 1
		else:
			s2 += 1
		t1_turn = not t1_turn

print(f"{name1} {s1} {name2} {s2}")
