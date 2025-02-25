import sys

N = int(sys.stdin.readline().rstrip())

X, Y = [], []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    X.append(x)
    Y.append(y)

points = sorted((Y[i], X[i]) for i in range(N))

for i in range(N):
    print(points[i][1], points[i][0])