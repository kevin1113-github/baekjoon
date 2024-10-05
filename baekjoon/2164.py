import sys
from collections import deque

N = int(sys.stdin.readline())

cards = [i for i in range(1, N+1)]
cards = deque(cards)

while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft())

print(cards[0])
