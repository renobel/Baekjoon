import sys

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = sys.stdin.readline().rstrip()
for i in range(26):
    if alp[i] in word:
        print(word.index(alp[i]), end=' ')
    else:
        print("-1", end=' ')