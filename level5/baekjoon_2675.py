import sys

n = int(sys.stdin.readline().rstrip())
results = []
for i in range(n):
    num, word = sys.stdin.readline().split()
    num = int(num)
    result = ""
    for j in range(len(word)):  
        result += word[j]*num
    results.append(result)

for i in range(n):
    print(results[i])
