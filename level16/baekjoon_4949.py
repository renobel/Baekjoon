import sys

open = []
result = []
while True:
    word = sys.stdin.readline().rstrip()
    if word == ".":
        break

    for i in word:
        if i == '(' or i == '[':
            open.append(i)
        elif i == ')':
            if len(open) != 0 and open[-1] == '(':
                open.pop(-1)
            else:
                open.append(1)
                break
        elif i == ']':
            if len(open) != 0 and open[-1] == '[':
                open.pop(-1)
            else:
                open.append(1)
                break
    if len(open) == 0:
        result.append("yes")
        open.clear()
    else:
        result.append("no")
        open.clear()

for data in result:
    print(data)