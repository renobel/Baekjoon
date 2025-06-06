import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
C = list(map(int, sys.stdin.readline().rstrip().split()))

QS = deque()
for i in range(N):
    if A[i] == 0:
        QS.append(B[i])

result = []

if len(QS) != 0:
    for i in range(M):
        result.append(QS.pop())
        QS.appendleft(C[i])
else:
    result = C

sys.stdout.write(" ".join(map(str, result))+"\n")