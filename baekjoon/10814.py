import sys

N = int(sys.stdin.readline())

members = [sys.stdin.readline().split() for _ in range(N)]

members.sort(key=lambda x: (int(x[0])))

print('\n'.join([' '.join(member) for member in members]))