import sys
n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} x {n2} = {n1 * n2}")
print(f"{n1} divided by {n2} is {int(n1/n2)} remainder {n1 - int(n1/n2)*n2}")
