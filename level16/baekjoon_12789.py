import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
buffer = []
n = 1
Good = True
for _ in range(N):
    if n in num:
        for _ in range(len(num)):
            i = num[0]
            if i == n:
                num.pop(0)
                break
            else:
                buffer.insert(0, num.pop(0))

    elif buffer[0] == n:
        buffer.pop(0)
    
    else:
        Good = False
        break
    n += 1

if Good:
    sys.stdout.write("Nice\n")
else:
    sys.stdout.write("Sad\n")
