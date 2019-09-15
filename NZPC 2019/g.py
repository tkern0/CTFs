"""
Thanks to this computerphile video that I randomly watched years ago I knew the exact way to do this
https://youtu.be/7ha78yWRDlE
"""

from sys import stdin

amount = int(stdin.readline())

for i in range(amount):
	numbers = []
	for val in stdin.readline()[:-1].split(" "):
		if val in "+-*/":
			if val == "+":
				n = numbers[-2] + numbers[-1]
			elif val == "-":
				n = numbers[-2] - numbers[-1]
			elif val == "*":
				n = numbers[-2] * numbers[-1]
			elif val == "/":
				n = int(numbers[-2] / numbers[-1])
			numbers = numbers[:-2]
			numbers.append(n)
		else:
			numbers.append(int(val))
	print(numbers[0])
