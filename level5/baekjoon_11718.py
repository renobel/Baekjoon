import sys

results = []
while 1:
    words = sys.stdin.readline().rstrip()
    if len(words) == 0:
        break
    results.append(words)
for i in range(len(results)):
    print(results[i])