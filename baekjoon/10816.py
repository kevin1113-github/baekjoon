import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

cardsDic = {}

for card in cards:
  if card in cardsDic:
    cardsDic[card] += 1
  else:
    cardsDic[card] = 1

for target in targets:
  if target in cardsDic:
    print(cardsDic[target], end=' ')
  else:
    print(0, end=' ')
