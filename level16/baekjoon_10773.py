import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

sys.stdout.write(f"{sum(stack)}\n")
