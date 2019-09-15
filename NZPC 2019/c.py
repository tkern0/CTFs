from sys import stdin

name = stdin.readline()[:-1]
num = int(stdin.readline())

ing = {}
for i in range(num):
	line = stdin.readline().split(", ")
	iName = line[0]
	iUnit = line[1]
	iAmount = float(line[2])

	if iUnit in ("kg", "l"):
		iAmount *= 1000
	
	ing[iName] = iAmount

have = {}
for i in range(num):
	line = stdin.readline().split(", ")
	iName = line[0]
	iUnit = line[1]
	iAmount = float(line[2])

	if iUnit in ("kg", "l"):
		iAmount *= 1000
	
	have[iName] = iAmount

need = set()
for i in ing:
	if have[i] < ing[i]:
		need.add(i)

if len(need) == 0:
	print(f"You may make your {name}.")
else:
	print(f"You may NOT make your {name}.")
	print(f"You need {', '.join(sorted(need))}.")
