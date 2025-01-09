import sys

result = []
while 1:
    num1, num2 = map(int,sys.stdin.readline().rstrip().split())
    if num1 == num2:
        break
    elif num1 % num2 == 0:
        result.append("multiple")
    elif num2 % num1 == 0:
        result.append("factor")
    else:
        result.append("neither")

for i in result:
    print(i)