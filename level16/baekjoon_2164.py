import sys

N = int(sys.stdin.readline().rstrip())
card = [i for i in range(1, N + 1)]

while len(card) != 1:
    if len(card) % 2 == 0:
        card = [card[i] for i in range(1,len(card), 2)]
    else:
        buffer = card[-1]
        card = [card[i] for i in range(1, len(card), 2)]
        card.insert(0, buffer)
print(card[0])