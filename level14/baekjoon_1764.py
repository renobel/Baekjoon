import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

N_list = set()
M_list = set()

for _ in range(N):
    N_list.add(sys.stdin.readline().rstrip())

for _ in range(M):
    M_list.add(sys.stdin.readline().rstrip())

result = N_list & M_list
result = sorted(list(result))
sys.stdout.write(f"{len(result)}\n"+"\n".join(result)+"\n")