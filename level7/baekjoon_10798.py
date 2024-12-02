import sys

result = []
length = 0
for i in range(5):
    arr = sys.stdin.readline().rstrip()
    if len(arr) > length:
        length = len(arr)
    result.append(arr)

for i in range(length):
    for j in range(5):
        try:
            print(result[j][i],end='')
        except:
            pass

print()
        


