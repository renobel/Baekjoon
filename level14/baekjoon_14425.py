import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

set_arr = set()

for i in range(N):
    set_arr.add(sys.stdin.readline().rstrip())

result = 0

for i in range(M):
    word = sys.stdin.readline().rstrip()
    if word in set_arr:
        result += 1

sys.stdout.write(str(result)+"\n")
# 집합과 딕셔너리 두 개를 모두 사용해본 결과, 성능(속도)에 큰 차이는 존재하지 않는다.