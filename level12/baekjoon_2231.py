import sys

N = int(sys.stdin.readline().rstrip())
result = 0

# 최대 9 * d 범위로 탐색 범위를 제한
start = max(1, N - 9 * len(str(N)))

for i in range(start, N):
    # 각 자리수를 더하면서 생성자 계산
    sum_of_digits = i
    temp = i
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10

    if sum_of_digits == N:
        result = i
        break

print(result)
