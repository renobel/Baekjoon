import sys

N, k = map(int, sys.stdin.readline().rstrip().split())

x = sys.stdin.readline().rstrip().split()
for i in range(N):
    x[i] = int(x[i])

x.sort()
print(x[N-k])