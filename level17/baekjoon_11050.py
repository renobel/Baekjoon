import sys

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return factorial(N-1)*N
    
N, K = map(int, sys.stdin.readline().rstrip().split())


sys.stdout.write(f"{factorial(N)//(factorial(K) * factorial(N-K))}\n")