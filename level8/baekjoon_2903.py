import sys 

n = int(sys.stdin.readline().rstrip())
dot = 2
for i in range(n):
    dot += 2**i

print(dot**2)