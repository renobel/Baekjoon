import sys

N = int(sys.stdin.readline().rstrip())

result = 0
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    
    buffer = []
    boolean = 0
    for i in range(len(word)):
        if i == 0:
            buffer.append(word[i])
            pre = word[i]
        else:
            if word[i] != pre and word[i] not in buffer:    #처음 보는 단어일때
                buffer.append(word[i])
                pre = word[i]
            elif word[i] != pre and word[i] in buffer:      #이미 나왔는데 또 나온 단어일때
                boolean = 1
            
    if boolean == 0:
        result += 1

print(result)
