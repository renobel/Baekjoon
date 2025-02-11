import sys

buffer = []

for _ in range(5):
    buffer.append(int(sys.stdin.readline().rstrip()))
    
buffer.sort()
print(sum(buffer)//len(buffer))
if len(buffer) % 2 == 0:
    print((buffer[len(buffer)//2]+buffer[len(buffer)//2 - 1])/2)
else:
    print(buffer[len(buffer)//2])