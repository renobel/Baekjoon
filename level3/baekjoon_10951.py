import sys

results = []
while (1):
  try:
    a, b = map(int, sys.stdin.readline().split())
    results.append(a + b)
  except:
    break

for i in range(len(results)):
  print(results[i])
