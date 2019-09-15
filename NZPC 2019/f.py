from sys import stdin

amount = int(stdin.readline())

C = ("R", "G", "B")
S = ("D", "O", "S")
N = ("1", "2", "3")
F = ("F", "S", "E")
O = (C, S, N, F)

for i in range(amount):
	a, b = stdin.readline().split(" ")

	out = ""

	for i in range(4):
		if a[i] == b[i]:
			out += a[i]
		else:
			t = list(O[i])
			t.remove(a[i])
			t.remove(b[i])
			out += t[0]

	print(out)
