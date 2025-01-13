import sys

angle = []
for _ in range(3):
    angle.append(int(sys.stdin.readline().rstrip()))

if angle[0] + angle[1] + angle[2] == 180:
    if angle[0] == angle[1] == angle[2] == 60:
        print("Equilateral")
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Error")