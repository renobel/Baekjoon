import sys

N = int(sys.stdin.readline().rstrip())

while N % 2 == 0:
    print(2)
    N //= 2

num = 3
while num * num <= N:
    while N % num == 0:
        print(num)
        N //= num
    num += 2

if N > 1:
    print(N)
