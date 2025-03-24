import sys 
import math

N = int(sys.stdin.readline().rstrip())
arr = []
result = []
for _ in range(N):
    num_1, num_2 = map(int, sys.stdin.readline().rstrip().split())
    arr.append((num_1, num_2))

for i,j in arr:
    result.append(str(math.lcm(i,j)))

sys.stdout.write("\n".join(result)+"\n")