import sys

Quadrant = {(1, 1): '1', (-1, 1): '2', (-1, -1): '3', (1, -1): '4'}

x = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
x = x / abs(x)
y = y / abs(y)
print(Quadrant[(x, y)])
