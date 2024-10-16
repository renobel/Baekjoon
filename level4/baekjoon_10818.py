import sys

N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

bigest = array[0]
smallest = array[0]
for i in range(N):
  if array[i] > bigest:
    bigest = array[i]
  if array[i] < smallest:
    smallest = array[i]

print(smallest, bigest)
