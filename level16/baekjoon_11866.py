import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(1,N + 1)]
result = []

ind = -1
while len(arr) != 0:
    ind += K
    while ind > len(arr) - 1:
        ind -= (len(arr))
    result.append(arr.pop(ind))
    ind -= 1

print("<",end='')
for num in result[:N-1]:
    print(f"{num}, ",end='')
print(f"{result[-1]}>")