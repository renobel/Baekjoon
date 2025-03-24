import sys

input = sys.stdin.readline
N = int(input())
arr = []

def check(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(N):
    num = int(input())
    arr.append(num)

for n in arr:
    while True:
        if check(n):
            print(n)
            break
        else:
            n += 1