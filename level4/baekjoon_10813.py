import sys

N, M = map(int, sys.stdin.readline().split())
basket = [(i + 1) for i in range(N)]

for var_1 in range(M):
  i, j = map(int, sys.stdin.readline().split())
  i, j = i - 1, j - 1
  temp = basket[i]
  basket[i] = basket[j]
  basket[j] = temp
for i in range(N):
  print(basket[i], end=' ')
