import sys

N = int(sys.stdin.readline().rstrip())
sorted = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    sorted.append(num)
    sorted.sort()

for i in range(len(sorted)):
    print(sorted[i])