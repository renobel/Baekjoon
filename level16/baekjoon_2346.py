import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
num_balloons = [i for i in range(1, N+1)]   #터뜨릴 풍선
rotate_balloons = deque(num_balloons)
balloons = list(map(int, sys.stdin.readline().rstrip().split())) #풍선 내용물

#처음 시작할 때   
point = balloons[0]    #첫 번째로 터트린 풍선 안의 번호를 저장한다.
result = [1]    #첫 번째로 터트린 풍선의 번호를 저장한다.    
rotate_balloons.popleft()
for _ in range(N-1):
    rotate_balloons.rotate(-((point - 1) if point > 0 else point))  #번호만큼 이동하기
    buf = rotate_balloons.popleft() #풍선 터뜨리기
    result.append(buf)  #풍선 번호 저장하기
    point = balloons[buf-1] #풍선 안의 번호를 저장하기

sys.stdout.write(" ".join(map(str, result))+"\n")