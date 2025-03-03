import sys

N = int(sys.stdin.readline().rstrip())

In_company = {}
result = []
for i in range(N):
    name, chk = sys.stdin.readline().rstrip().split()
    if chk == "enter":
        In_company[name] = 1
    else:
        In_company[name] = 0
    
for i in In_company:
    if In_company[i] == 1:
        result.append(i)

result.sort(reverse=True)
sys.stdout.write("\n".join(result)+"\n")
#remove() 사용하지 마. 겁나 느려