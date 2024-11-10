import sys

word_list = {}
word = sys.stdin.readline().rstrip()
for i in range(len(word)): 
    part = ord(word[i])
    if part > 64 and part < 96:
        part += 32
    if part in word_list:
        word_list[part] += 1
    else:
        word_list[part] = 1

