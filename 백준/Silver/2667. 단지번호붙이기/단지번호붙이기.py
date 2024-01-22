def dfs(x, y):
    global cnt
    graph[x][y] = 0
    cnt += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for count in result:
    print(count)
