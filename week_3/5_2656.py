import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def dfs(u):
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            dfs(v)

count = 0

dfs(1)

print(sum(visited) - 1)
