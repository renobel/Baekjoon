import sys

studentNums = [(i + 1) for i in range(30)]
for i in range(28):
  studentNums.remove(int(sys.stdin.readline().rstrip()))
print(f"{studentNums[0]}\n{studentNums[1]}")
