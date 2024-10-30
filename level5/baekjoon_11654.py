import sys

data = sys.stdin.readline().rstrip()
try:
    print(ord(data))
except:
    print(chr(int(data)))