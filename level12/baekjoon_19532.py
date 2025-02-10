import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())

if b != 0:
    x = (b*f - c*e) // (b*d - a*e)
    y = int(-(a/b)*x + c/b)
else:
    x = (b*f - c*e) // (b*d - a*e)
    y = int(-(c*d/(a*e)) + f/e)

print(x, y)

#ax + by = c
#dx + ey = f