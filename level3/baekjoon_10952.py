import sys

results = []
while (1):
  a, b = map(int, sys.stdin.readline().split())
  if a == 0 and b == 0:
    break
  results.append(a + b)

for i in range(len(results)):
  print(results[i])
