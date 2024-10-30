import sys

n_1, n_2 = sys.stdin.readline().split()
n_1 = int(n_1[::-1])
n_2 = int(n_2[::-1])
if n_1 > n_2:
    print(n_1)
else:
    print(n_2)