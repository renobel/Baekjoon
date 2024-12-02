import sys

Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().rstrip()
result = 0
i = 0
CroatiaWord = Croatia[i]
while i < len(Croatia):
    CroatiaWord = Croatia[i]
    if CroatiaWord in word:
        WordIndex = word.find(CroatiaWord)
        word = list(word)
        word = word[:WordIndex] + [" "] + word[WordIndex+len(CroatiaWord):]
        word = "".join(word)
        result += 1
    else:
        i+=1
word = list(word)
j = 0
while j < len(word):
    if word[j] == " ":
        del word[j]
    else:
        j += 1
word = "".join(word)
for i in range(len(word)):
    result += 1
        
print(result)