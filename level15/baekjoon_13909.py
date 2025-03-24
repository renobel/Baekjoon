import sys

N = int(sys.stdin.readline().rstrip())
window = [0] * (N + 1)

for man in range(1, N+1):
    for check in range(man, N + 1, man):
        if window[check] == 0:
            window[check] = 1
        else:
            window[check] = 0
        
result = 0
for check in window[1:]:
    if check == 1:
        result += 1

sys.stdout.write(str(result)+"\n")