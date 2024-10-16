import sys

N, X = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
int_less = []
for i in range(N):
  if array[i] < X:
    int_less.append(array[i])

for i in range(len(int_less)):
  print(int_less[i], end=' ')
