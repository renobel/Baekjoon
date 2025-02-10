import sys

N = int(sys.stdin.readline().rstrip())

five = N // 5
three = (N % 5) % 3
success = 0

for _ in range(3):
    if three == 0:
        success = 1
        break
    else:
        if N - (5 * five) <= 0 or five == 0:
            pass
        else:
            five -= 1
            three = (N - (5 * five)) % 3
        
if success == 1:
    print(five+((N - (5 * five)) // 3))
else:
    print(-1)