import sys

N = int(sys.stdin.readline().rstrip())
Dict = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    Dict.append((a, b, a + b))

for i in range(N):
    num1, num2, result = Dict[i]
    print(f"Case #{i+1}: {num1} + {num2} = {result}")
