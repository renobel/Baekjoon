import sys

list = []
for i in range(10):
  num = int(sys.stdin.readline().rstrip())
  if not num % 42 in list:
    list.append(num % 42)
print(len(list))
