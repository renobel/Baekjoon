import sys
import math

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
factors = []

for num in range(M, N+1):
    chk = 0
    if num != 1:
        for  i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                chk = -1
                break
        if chk == 0:
            factors.append(num)

if len(factors) == 0:
    print(-1)

else:
    print(sum(factors))
    print(factors[0])