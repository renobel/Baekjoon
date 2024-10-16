import sys


def dice(list):
    if list[0] == list[1] and list[1] == list[2]:
        return 10000 + list[0] * 1000
    elif list[0] == list[1] or list[1] == list[2]:
        return 1000 + list[1] * 100
    else:
        return list[2] * 100


a, b, c = map(int, sys.stdin.readline().split())
list = [a, b, c]
list.sort()

print(dice(list))
