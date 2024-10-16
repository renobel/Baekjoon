import sys

gun_amount = int(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
pay_list = []
sum = 0
for i in range(num):
    pay, count = map(int, sys.stdin.readline().split())
    pay_list.append(pay * count)
    sum += pay_list[i]
if gun_amount == sum:
    print("Yes")
else:
    print("No")
