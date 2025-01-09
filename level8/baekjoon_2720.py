import sys

n = int(sys.stdin.readline().rstrip())

result = []
change = [25,10,5,1]
for _ in range(n):
    cent = int(sys.stdin.readline().rstrip())
    output = []
    for i in range(4):
        output.append(cent//change[i])
        cent = cent % change[i]
    result.append(output)

for i in range(len(result)):
    for j in range(4):
        print(result[i][j],end=' ')
    print()