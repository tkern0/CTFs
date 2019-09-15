import sys

total = 0
output = ""
for line in sys.stdin:
  if line == "\n":
    break
  i = int(line)
  total += i
  output += f"N = {i: <10}Partial Sum = {total}\n"

f_len = 15 + len(str(total))
output = output[:-f_len] + f"Final Sum   = {total}"
print(output)
