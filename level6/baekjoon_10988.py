import sys

word = sys.stdin.readline().rstrip()
i = 0
result = 1
while i < len(word)-1-i:
    if word[i] != word[len(word)-1-i]:
        result = 0
        break
    else:
        result = 1
    i += 1
print(result)
#처음에 result = 0 으로 초기화했을 때에는 문제가 오답이었는데 그 이유를 모르겠다.
#입력 문자의 길이가 1일 때, 즉 단어가 하나만 들어왔을 때 반복문을 수행하지 않아 오류가 발생하는 것을 확인했다.