"""
When reading over the description to this problem it first seemed quite simple - it's just adding
 base 62 numbers together.
Unfortauntly I quickly realized that that doesn't quite work out - the offset is only for valid
 passwords, if you just add numbers you'll go through plenty of invalid ones that shouldn't count
A quick trial adding one at a time proved to be too slow so I quickly abandoned this
"""

from sys import stdin

L = int(stdin.readline())
D, U, S = stdin.readline().split(" ")
D = int(D)
U = int(U)
S = int(S)

K = int(stdin.readline()) - 1

alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

next = {
"0": "1",
"1": "2",
"2": "3",
"3": "4",
"4": "5",
"5": "6",
"6": "7",
"7": "8",
"8": "9",
"9": "A",
"A": "B",
"B": "C",
"C": "D",
"D": "E",
"E": "F",
"F": "G",
"G": "H",
"H": "I",
"I": "J",
"J": "K",
"K": "L",
"L": "M",
"M": "N",
"N": "O",
"O": "P",
"P": "Q",
"Q": "R",
"R": "S",
"S": "T",
"T": "U",
"U": "V",
"V": "W",
"W": "X",
"X": "Y",
"Y": "Z",
"Z": "a",
"a": "b",
"b": "c",
"c": "d",
"d": "e",
"e": "f",
"f": "g",
"g": "h",
"h": "i",
"i": "j",
"j": "k",
"k": "l",
"l": "m",
"m": "n",
"n": "o",
"o": "p",
"p": "q",
"q": "r",
"r": "s",
"s": "t",
"t": "u",
"u": "v",
"v": "w",
"w": "x",
"x": "y",
"y": "z",
"z": "0",
}

def addOffset(base, K):
	if K == -1:
		return base

	out = ""
	charIndex = len(base) - 1
	while K != 0:
		char = base[charIndex]

		val = 0
		for i in range(len(alph)):
			if alph[i] == char:
				val = i
				break

		shift = K % 62
		K = int(K/62)

		val = val + shift
		while val > 62:
			val -= 62

		out = alph[val] + out
		charIndex -= 1
	return out

def addOne(base):
	char = base[-1]
	out = ""
	i = -2
	while char == "z":
		char = base[i]
		out = "0" + out
		i -= 1
	return base[:i + 1] + next[char] + out


base = "0" * (L-U-S) + "A" * U + "a" * S

#out = addOffset(base, K)
out = base
while K > 0:
	out = addOne(out)
	dc = 0
	uc = 0
	sc = 0
	for char in out:
		if "0" <= char <= "9":
			dc += 1
		elif "A" <= char <= "Z":
			uc += 1
		elif "a" <= char <= "z":
			sc += 1
	if dc >= D and uc >= U and sc >= S:
		K -= 1
print(out)
