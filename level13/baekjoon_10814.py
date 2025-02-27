import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    arr.append([int(age), i, name])

arr.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(int(arr[i][0]), arr[i][2])