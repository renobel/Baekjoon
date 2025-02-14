import sys

def QuickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    left, middle, right = [], [], []
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] == pivot:
            middle.append(array[i])
        else:
            right.append(array[i])
    return QuickSort(left) + middle + QuickSort(right)

N = int(sys.stdin.readline().rstrip())

num = []
for _ in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

num = QuickSort(num)
for i in range(N):
    print(num[i])