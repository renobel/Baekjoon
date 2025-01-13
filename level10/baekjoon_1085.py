import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

side = w - x if x >= (w/2) else x

height = h - y if y >= (h / 2) else y

print(height) if side >= height else print(side)