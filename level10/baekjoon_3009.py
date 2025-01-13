import sys

point_x, point_y = {}, {}

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x not in point_x:
        point_x[x] = 1
    else:
        point_x[x] += 1
    
    if y not in point_y:
        point_y[y] = 1
    else:
        point_y[y] += 1
    
x = [k for k, v in point_x.items() if v == 1]
y = [k for k, v in point_y.items() if v == 1]
print(x[0], y[0])