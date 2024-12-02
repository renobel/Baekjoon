import sys

word = sys.stdin.readline().rstrip()
word_list = list(set(word))
result = []

for i in word_list:
    num = word_list.count(i)
    result.append(num)

if result.count(max(result))>=2:
    print("?")
else:
    print(word_list[result.index(max(result))])
#아 개어렵다 ㅠ