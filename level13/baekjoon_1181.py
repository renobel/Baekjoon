import sys

N = int(sys.stdin.readline().rstrip())

word = set()  # 중복 제거를 위한 set 사용
for _ in range(N):
    word.add(sys.stdin.readline().rstrip())  # O(1) 평균 시간으로 중복 체크

# 정렬 기준: (길이, 사전 순)
arr = sorted(word, key=lambda x: (len(x), x))

# 결과 출력
sys.stdout.write("\n".join(arr)+"\n")