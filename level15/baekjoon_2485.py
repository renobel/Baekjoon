import sys
import math
N = int(sys.stdin.readline().rstrip())
dis = []

for _ in range(N):
    dis.append(int(sys.stdin.readline().rstrip()))

arr = []
pre = dis[0]
for present in dis[1:]:
    arr.append(present - pre)
    pre = present

gcd = math.gcd(*arr)
n = 0
for i in arr:
    n += i//gcd - 1

sys.stdout.write(str(n)+"\n")
