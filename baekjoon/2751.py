import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

print(*sorted(numbers))