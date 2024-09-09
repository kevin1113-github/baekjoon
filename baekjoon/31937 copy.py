from collections import defaultdict, deque

def find_initial_infected_computer(N, M, K, infected_computers, logs):
    # 그래프 생성 (전파 경로: a -> b로 전파)
    graph = defaultdict(list)
    
    # 로그는 시간순으로 주어지므로 그대로 그래프를 생성
    for t, a, b in logs:
        graph[a].append(b)  # a에서 b로 파일 전송, 즉 a에서 b로 전파됨
    
    # 감염된 컴퓨터들의 집합
    infected_set = set(infected_computers)

    # 감염된 컴퓨터들 중 최초 감염자가 될 가능성이 있는 컴퓨터들을 찾는 함수
    def bfs(start):
        queue = deque([start])
        visited = set([start])
        while queue:
            current = queue.popleft()
            # 현재 노드로부터 감염된 노드를 탐색
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor in infected_set:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    # 첫 번째 감염 컴퓨터에서 시작하여 역방향으로 탐색
    initial_candidates = bfs(infected_computers[0])
    
    # 모든 감염된 컴퓨터에 대해 역추적하여 최초 감염자 후보를 찾음
    for comp in infected_computers[1:]:
        initial_candidates &= bfs(comp)
    
    # 최초 감염자 후보 중 가장 작은 번호 반환
    return min(initial_candidates)

# 입력 처리
N, M, K = map(int, input().split())
infected_computers = list(map(int, input().split()))
logs = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
print(find_initial_infected_computer(N, M, K, infected_computers, logs))
