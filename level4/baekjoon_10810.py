import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0 for _ in range(N)]
for var_1 in range(M):
  i, j, k = map(int, sys.stdin.readline().split())
  for var_2 in range(i, j + 1):
    basket[var_2 - 1] = k
for i in range(N):
  print(basket[i], end=' ')
