import sys

N = int(sys.stdin.readline().rstrip())
results = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    results.append(a + b)

for i in range(N):
    print(f"Case #{i+1}: {results[i]}")
