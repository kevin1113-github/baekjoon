import sys

N = int(sys.stdin.readline())
cards = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())
numbers = sys.stdin.readline().split()

print(*[1 if number in cards else 0 for number in numbers], sep=' ')