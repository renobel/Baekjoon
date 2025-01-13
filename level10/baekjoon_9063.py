import sys

N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(0)
else:
    point_x, point_y = [], []
    for _ in range(N):
        data_x, data_y = map(int,sys.stdin.readline().rstrip().split())
        point_x.append(data_x)
        point_y.append(data_y)

    min_x = min(point_x)
    min_y = min(point_y)
    max_x = max(point_x)
    max_y = max(point_y)

    print((max_x - min_x) * (max_y - min_y))