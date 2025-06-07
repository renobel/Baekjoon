import sys

N = int(sys.stdin.readline().rstrip())
if N == 1:
    sys.stdout.write("0\n")

else:
    sys.stdout.write(f"{N*(N-1)}\n")