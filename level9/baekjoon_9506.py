import sys

result = []
while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    factor = []
    for i in range(1,n//2 + 1):
        if n % i == 0:
            if i not in factor:
                factor.append(i)
                if i**2 != n:
                    factor.append(n // i)
    factor.sort()
    result.append([n,factor])

for i in range(len(result)):
    sum = 0
    for j in range(len(result[i][1])-1):
        sum += result[i][1][j]
    if result[i][0] == sum:
        print(f"{result[i][0]} =",end='')
        for j in range(len(result[i][1])-1):
            if j == len(result[i][1])-2:
                print(f" {result[i][1][j]}")
            else:
                print(f" {result[i][1][j]} +",end='')
    else:
        print(f"{result[i][0]} is NOT perfect.")
