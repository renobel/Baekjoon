import sys

score = int(sys.stdin.readline())
grades = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}
print(grades.get(score // 10, 'F'))
