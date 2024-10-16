import sys

count = int(sys.stdin.readline().rstrip())
list = []
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a + b)

for i in list:
    print(i)
