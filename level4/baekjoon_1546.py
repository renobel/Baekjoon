import sys

N = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().split()))
max = 0
for i in range(N):
    if scores[i] > max:
        max = scores[i]

sum = 0
for i in range(N):
    sum += ((scores[i]/max) * 100)

print(sum/N)