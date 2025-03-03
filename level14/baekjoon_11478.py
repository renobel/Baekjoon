import sys

word = sys.stdin.readline().rstrip()
result = set()
for i in range(len(word)):
    for j in range(i,len(word)):
        result.add(word[i:j+1])

sys.stdout.write(str(len(result))+"\n")