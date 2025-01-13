import sys

lengths = sorted(map(int,sys.stdin.readline().rstrip().split()))

while lengths[2] >= lengths[0] + lengths[1]:
    lengths[2] -= 1

print(lengths[0] + lengths[1] + lengths[2])