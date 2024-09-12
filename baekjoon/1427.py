import sys

N = list(sys.stdin.readline().strip())

N = list(map(int, N))
N.sort(reverse=True)

print(*N, sep='')