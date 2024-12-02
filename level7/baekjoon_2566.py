import sys

tdl = []
for i in range(9):
    tdl.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [0,0,0]
for i in range(9):
    for j in range(9):
        if tdl[i][j] >= result[0]:
            result[0] = tdl[i][j]
            result[1] = i + 1
            result[2] = j + 1

print(result[0])
print(result[1],result[2])
    