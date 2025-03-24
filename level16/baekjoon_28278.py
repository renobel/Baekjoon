import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    data = sys.stdin.readline().rstrip()
    if len(data) != 1:
        num, X = data.split()
        num = int(num)
        X = int(X)
    else:
        num = int(data)

    if num == 1:
        stack.append(X)

    elif num == 2:
        if len(stack) != 0:
            sys.stdout.write(f"{stack.pop()}\n")
        else:
            sys.stdout.write("-1\n")

    elif num == 3:
        sys.stdout.write(f"{len(stack)}\n")

    elif num == 4:
        if len(stack) != 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write("1\n")

    elif num == 5:
        if len(stack) != 0:
            sys.stdout.write(f"{stack[len(stack)-1]}\n")
        else:
            sys.stdout.write("-1\n")