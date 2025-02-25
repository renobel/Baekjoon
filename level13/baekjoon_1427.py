import sys

N = list(map(str, sys.stdin.readline().rstrip()))
num = []

for _ in range(len(N)):
    num.append(max(N))
    N.remove(max(N))

result = ''.join(num)
print(int(result))
