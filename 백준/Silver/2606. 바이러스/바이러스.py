from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(start):
    count = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        x = queue.popleft()
        for neighbor in graph[x]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1

    return count

result = bfs(1)
print(result)