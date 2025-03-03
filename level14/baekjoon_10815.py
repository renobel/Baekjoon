import sys

N = int(sys.stdin.readline().rstrip())
SG = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().rstrip().split()))

dic = {}
for i in range(N):
    dic[SG[i]] = 0

for i in range(M):
    if comp[i] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ') 