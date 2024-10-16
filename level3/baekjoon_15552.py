import sys

results = []
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    results.append(a + b)

for i in results:
    print(i)
