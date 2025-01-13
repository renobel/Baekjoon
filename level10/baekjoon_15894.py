import sys

n = int(sys.stdin.readline().rstrip())
print(4 * n)

"""
n = 1 -> 4
n = 2 -> (4 - 1) + 4 + 1 = 8
n = 3 -> (8 - 2) + 5 + 1 = 12
n = 4 -> (12 - 3) + 6 + 1 = 16
"""