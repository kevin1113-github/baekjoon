import sys
from collections import deque

def DFS(t):
  log = logs[t]
  # if not(log[0] in infected and log[1] in infected):
  #   return [-1]
  G = deque()
  G.append(log[1])
  if t+1 < M:
    for i in range(t+1, M):
      if logs[i][0] == log[1]:
        # child = DFS(i)
        # if child == [-1]: return [-1]
        # else: G.extend(DFS(i))
        G.extend(DFS(i))
  return list(G)

N, M, K = list(map(int, sys.stdin.readline().split()))
infected = list(map(int, sys.stdin.readline().split()))
logs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
logs.sort(key= lambda x: x[0])
logs = list(map(lambda x: x[1:], logs))

root = 0
infect_set = set(infected)
for i in range(M):
  log = logs[i]
  if log[0] in infected and log[1] in infected:
    # print(DFS(i) + [log[0]])
    if infect_set == set(DFS(i) + [log[0]]):
      root = i+1
      break
print(root)

# 위에서 부터 아래로 내려감
# 감염 된 컴퓨터로 전송 된 파일 로그를 발견하면
# 해당 그래프 전체 탐색
# 해당 그래프의 모든 노드가 set 을 씌웠을 때 infected와 일치하면
# 해당 그래프의 루트 노드가 정답.

# 그래프 전체 탐색
# DFS: 