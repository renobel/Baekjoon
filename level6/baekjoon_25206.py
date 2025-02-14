import sys

score = 0
credit = 0
dic = {"F": 0, "D0": 1.0, "D+": 1.5, "C0": 2.0, "C+": 2.5, "B0": 3.0, "B+": 3.5, "A0": 4.0, "A+": 4.5}

for _ in range(20):
    Class = sys.stdin.readline().rstrip().split()
    if Class[2] != "P":
        credit += float(Class[1])
        score += float(Class[1]) * dic[Class[2]]

print(score/credit)