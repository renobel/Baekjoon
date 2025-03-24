import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    is_VPS = True
    buffer = []
    for i in data:
        if i == "(":
            buffer.append("(") 
        else:
            if len(buffer) == 0:
                is_VPS = False
                break
            else:
                buffer.pop()
    if len(buffer) != 0:
        is_VPS = False
    
    if is_VPS:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
