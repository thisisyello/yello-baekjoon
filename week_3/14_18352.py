from collections import deque
import sys
input = sys.stdin.readline

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def add(self, u, v, w = 1):
        self.graph[u].append((v, w))

    def bfs(self, current, visited = None):
        if visited is None:
            visited = [-1] * self.size
        q = deque([])
        q.append(current)
        visited[current] = 0

        while q:
            current = q.popleft()

            for nxt, _ in self.graph[current]:
                if visited[nxt] == -1:
                    visited[nxt] = visited[current] + 1
                    q.append(nxt)

        return visited

# n = 도시 / m = 도로 / k = 거리 / x = 도시 번호
n, m, k, x = map(int,input().split())
g = Graph(n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    g.add(a, b)

dist = g.bfs(x)
ans = [i for i in range(1, n + 1) if dist[i] == k]

if ans:
    print('\n'.join(map(str, sorted(ans))))
else:
    print(-1)
