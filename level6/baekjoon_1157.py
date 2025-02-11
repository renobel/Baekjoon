#내가 짠 코드
"""import sys

word = list(sys.stdin.readline().rstrip())

for i in range(len(word)):
    if ord(word[i]) >= 97 and ord(word[i]) <= 122:
        word[i] = chr(ord(word[i])-32)
    
buffer = {}
cnt = []    #단어 개수 저장
result = [] #단어와 개수 저장
for i in range(len(word)):
    if word[i] not in buffer:
        buffer[word[i]] = word.count(word[i])
        result.append([word[i],buffer[word[i]]])

for i in range(len(result)):
    cnt.append(result[i][1])

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(result[cnt.index(max(cnt))][0])
"""
#다른 사람이 짠 코드
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])
"""
upper 함수를 쓸 줄 알아야 한다.
set 함수를 쓸 줄 알아야 한다.
"""