import sys

sys.stdin.readline()
day1 = sys.stdin.readline()
day2 = sys.stdin.readline()
count = 0
for i in range(len(day1)):
	if day1[i] == "O" and day2[i] == "O":
		count += 1

print(count)



