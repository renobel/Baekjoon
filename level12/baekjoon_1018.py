import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
result = []

for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1

                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))
#출처 티스토리
#혼자 코딩하다가 머리 터질 것 같아서 참고함
#문제해결을 위해 접근하는 방법을 다르게 할 필요가 있다는 것을 깨달음