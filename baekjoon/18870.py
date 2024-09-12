import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

X_set = sorted(list(set(X)))

X_dict = {X_set[i]: i for i in range(len(X_set))}

print(*[X_dict[x] for x in X])