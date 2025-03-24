import sys
import math

son_a, mother_a = map(int, sys.stdin.readline().rstrip().split())
son_b, mother_b = map(int, sys.stdin.readline().rstrip().split())

A = son_a*mother_b + son_b*mother_a
B = mother_a*mother_b

gcd = math.gcd(A, B)
if gcd != 1:
    A //= gcd
    B //= gcd

sys.stdout.write(f"{str(A)} {str(B)}\n")