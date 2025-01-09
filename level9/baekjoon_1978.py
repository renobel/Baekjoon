import sys
import math

N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for i in range(N):
    chk = 0
    if nums[i] == 1:
        pass
    else:
        for j in range(2, int(math.sqrt(nums[i]))+1):
            if nums[i] % j == 0:
                chk = -1
        if chk == 0:
            result += 1

print(result)
