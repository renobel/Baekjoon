import sys

max_index = 0
max_value = None
for i in range(9):
  num = int(sys.stdin.readline().rstrip())
  if max_value == None:
    max_value = num
    max_index = i + 1
    continue
  else:
    if num > max_value:
      max_value = num
      max_index = i + 1

print(f"{max_value}\n{max_index}")
