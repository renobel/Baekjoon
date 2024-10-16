import sys

hour, minute = map(int, sys.stdin.readline().split())
cookingtime = int(sys.stdin.readline())
if minute + cookingtime >= 60:
    hour += (minute + cookingtime) // 60
    minute = (minute + cookingtime) % 60
else:
    minute += cookingtime
if hour > 23:
    hour -= 24

print(hour, minute)
