import sys

N, M = map(int, sys.stdin.readline().split())

N_list = [sys.stdin.readline().strip() for _ in range(N)]
M_list = [sys.stdin.readline().strip() for _ in range(M)]

result = sorted(list(set(N_list) & set(M_list)))
print(len(result))
print(*result, sep='\n')
