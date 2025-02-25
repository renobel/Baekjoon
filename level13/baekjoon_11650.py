import sys

N = int(sys.stdin.readline().rstrip())

X = []  #X 좌표
Y = []  #Y 좌표

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())  
    X.append(x)
    Y.append(y)

points = sorted((X[i], Y[i], i) for i in range(N))

for i in range(N):
    print(points[i][0], points[i][1])