import sys

N = int(sys.stdin.readline().rstrip())
sum = 0
for i in range(N):
    sum += i + 1

print(sum)
