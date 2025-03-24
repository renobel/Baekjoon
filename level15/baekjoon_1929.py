import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

for num in range(N, M + 1):
    bin = 0
    if num < 2:
        continue
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            bin = 1
            break
    if bin == 0:
        print(num)