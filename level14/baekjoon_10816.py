import sys

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().rstrip().split()))

result = {}
result_2 = []
for i in M_list:
    result[i] = 0

for i in N_list:
    if i in result:
        result[i] += 1

for i in M_list:
    result_2.append(str(result[i]))
sys.stdout.write(" ".join(result_2)+"\n")