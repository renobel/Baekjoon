import sys

num = int(sys.stdin.readline().rstrip())

current = 2
i = 1
while 1:
    if num == 1:
        print(1)
        break
    else:
        if num < current:
            print(i)
            break
        else:
            current += 6*i
            i += 1
