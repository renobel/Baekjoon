import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

card.sort()
result = 0

for i in range(N - 2):
    left, right = i + 1, N - 1  # 투 포인터 초기화
    while left < right:
        total = card[i] + card[left] + card[right]

        if total > M:  # 합이 M을 초과하면, right를 줄여야 함
            right -= 1
        else:  # 합이 M 이하이면, 최대값을 갱신하고 left를 증가
            result = max(result, total)
            left += 1

print(result)
