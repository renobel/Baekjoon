import sys

pieces = [1, 1, 2, 2, 2, 8]
pieces_input = list(map(int, sys.stdin.readline().split()))
pieces_result = []
for i in range(6):
    pieces_result.append(pieces[i] - pieces_input[i])
    print(pieces_result[i], end=' ')
print()