import sys

n = int(sys.stdin.readline().rstrip())
data = sys.stdin.readline().rstrip()
result = 0
for i in range(n):
    result += int(data[i])
print(result)