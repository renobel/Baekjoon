import math
import sys 

# 입력받기
A, B, V = map(int, sys.stdin.readline().rstrip().split())
days = math.ceil((V - A) / (A - B)) + 1

print(days)