import sys

# N: 학생 수, k: 등수
N, k = map(int, sys.stdin.readline().split())

# x: 학생들의 점수
x = list(map(int, sys.stdin.readline().split()))

# k번째로 높은 점수 출력 (커트라인)
print(sorted(x, reverse=True)[k-1])
