import sys

n = int(sys.stdin.readline().rstrip())
results = []
for i in range(n):
    data = sys.stdin.readline().rstrip()
    results.append(f"{data[0]}{data[len(data)-1]}")
for i in range(n):
    print(results[i])