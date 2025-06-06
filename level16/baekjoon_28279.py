import sys
from collections import deque

DQ = deque()
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    order = sys.stdin.readline().rstrip().split()
    order[0] = int(order[0])
    if order[0] == 1:
        DQ.appendleft(int(order[1]))
    
    if order[0] == 2:
        DQ.append(int(order[1]))

    if order[0] == 3:
        if len(DQ) != 0 and type(DQ[0]) == int:
            print(DQ.popleft())
        else:
            print(-1)

    if order[0] == 4:
        if len(DQ) != 0 and type(DQ[-1]) == int:
            print(DQ.pop())
        else:
            print(-1)

    if order[0] == 5:
        print(len(DQ))

    if order[0] == 6:
        if len(DQ) == 0:
            print(1)
        else:
            print(0)

    if order[0] == 7:
        if len(DQ) != 0 and type(DQ[0]) == int:
            print(DQ[0])
        else:
            print(-1)

    if order[0] == 8:
        if len(DQ) != 0 and type(DQ[-1]) == int:
            print(DQ[-1])
        else:
            print(-1)