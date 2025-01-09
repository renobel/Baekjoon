import sys 

num = int(sys.stdin.readline().rstrip())
i, j = 1, 1
while num > i:
    j += 1
    i += j

num = num - i + j
if j % 2:
    i = j
    j = 1
    for _ in range(num-1):
        j += 1
        i -= 1
else:
    i = 1
    for _ in range(num-1):
        j -= 1
        i += 1
        
print(f"{i}/{j}")
