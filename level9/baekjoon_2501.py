import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
result = []

for i in range(1, N//2 + 1):
    if N % i == 0:
        if i not in result:
            result.append(i)
            if i**2 != N:
                result.append(N // i)

result.sort()
if len(result) < M:
    print(0)
else:
    print(result[M-1])

