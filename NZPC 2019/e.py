from sys import stdin

w1, w2, w3, w4, w5 = [int(i) for i in stdin.readline().split(" ")]
S = int(stdin.readline())

total = sum([w1, w2, w3, w4, w5]) * 10

students = {}
student_order = []
for i in range(S):
	line = stdin.readline()
	name = line[5:-1]
	students[line[:4]] = name
	student_order.append(name)

attempts = {}
points = {}
for line in stdin:
	if line == "0 # #\n":
		break
	
	sid, eid, r = line.split(" ")

	if sid not in attempts:
		attempts[sid] = {}

	if eid not in attempts[sid]:
		attempts[sid][eid] = 0

	attempts[sid][eid] += 1

	if r == "F\n":
		continue

	weight = 1
	if eid == "A":
		weight = w1
	elif eid == "B":
		weight = w2
	elif eid == "C":
		weight = w3
	elif eid == "D":
		weight = w4
	elif eid == "E":
		weight = w5

	c = attempts[sid][eid]

	mark = 4
	if c == 1:
		mark = 10
	elif c == 2:
		mark = 7

	name = students[sid]
	if name not in points:
		points[name] = 0
	points[name] += weight * mark

for s in student_order:
	message = "Fail"
	if s in points and points[s] >= total/2:
		message = "Pass"

	print(f"{s} {message}")
	

