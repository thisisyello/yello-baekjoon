import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# n = 정점의 개수, m = 간선의 개수
n, m = map(int, input().split())
# 인접리스트 생성
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    # 간선의 양 끝점
    u, v = map(int, input().split())
    # 무방향 그래프
    graph[u].append((v)) # u에 v 연결
    graph[v].append((u)) # v에 u 연결

# 방문 여부를 기록하는 배열
# False로 초기화하고 visited[i] = True면 방문
visited = [False] * (n + 1)

def dfs(u):
    # 현재 정점 방문 처리
    visited[u] = True
    # u와 연결된 모든 정점 v에 대해
    for v in graph[u]:
        # 아직 방문하지 않았다면
        if not visited[v]:
            # v 방문처리
            dfs(v)

# 간선의 개수
count = 0

# 1번 정점부터 n번 정점까지 검사
for i in range(1, n + 1):
    # 만약 아직 방문하지 않았다면
    if not visited[i]:
        dfs(i) # 그 정점에서 DFS 실행 -> 같은 덩어리(연결요소) 다 방문됨
        count += 1 # 간선 하나 발견했으니 개수 +1
    print(graph[i])

print(count)