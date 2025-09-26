import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def add(self, u, v):
        self.graph[u].append((v, 1))
        self.graph[v].append((u, 1))

    def dfs(self, current, parent, visited = None):
        # if visited is None:
        #     visited = [False] * self.size
        
        visited[current] = True

        for nxt, _ in self.graph[current]:
            if not visited[nxt]:
                parent[nxt] = current
                self.dfs(nxt, parent, visited)

n = int(input())
g = Graph(n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    g.add(a, b)

visited = [False] * (n + 1)
parent = [0] * (n + 1)

g.dfs(1, parent, visited)

print('\n'.join(str(parent[i]) for i in range(2, n + 1)))
