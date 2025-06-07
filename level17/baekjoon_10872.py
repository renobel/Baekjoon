import sys

def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return factorial(N-1)*N
    
N = int(sys.stdin.readline().rstrip())
sys.stdout.write(f"{factorial(N)}\n")