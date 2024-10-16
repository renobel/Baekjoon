import sys

N, M = map(int,sys.stdin.readline().split())
basket = [(i+1) for i in range(N)]
for var_1 in range(M):
    i, j = map(int, sys.stdin.readline().split())
    num = 0
    while 1:
        if not (i + num) >= (j-num):
            temp = basket[i + num - 1] 
            basket[i + num - 1] = basket[j - num - 1]
            basket[j - num - 1] = temp
            num += 1
        else:
            break
        
for i in range(N):
     print(basket[i], end=' ')