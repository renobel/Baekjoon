import sys

check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in arr:
    result = 0
    for j in range(2, i//2 + 1):
        if check[j] == 0 and check[i-j] == 0:
            result += 1
    print(result)