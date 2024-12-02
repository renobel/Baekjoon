import sys

paper = [[1 for _ in range(100)] for _ in range(100)]
num = int(sys.stdin.readline().rstrip())
for _ in range(num):
    side, height = map(int,sys.stdin.readline().rstrip().split())
    for i in range(height, height+10):
        for j in range(side, side + 10):
            paper[i][j] = 0

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 0:
            cnt += 1
        
print(cnt)
        