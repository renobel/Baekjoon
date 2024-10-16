import sys

N = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().split()))

search = int(sys.stdin.readline().rstrip())

count = 0

for i in range(len(array)):
  if array[i] == search:
    count += 1

print(count)
