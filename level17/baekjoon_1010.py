import sys

def factorial(N):
    num = 1
    for n in range(1, N+1):
        num *= n

    return num    

N = int(sys.stdin.readline().rstrip())
case = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    case.append([A, B])

i = 0
for test in case:
    case[i] = factorial(test[1])//(factorial(test[0]) * factorial(test[1]-test[0]))
    i += 1

for out in case:
    print(out)