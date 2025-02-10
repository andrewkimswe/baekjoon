import sys

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(1)

print(sum(visited) - 1)