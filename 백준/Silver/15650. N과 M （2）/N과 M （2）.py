N, M = map(int, input().split())
list = []

def dfs(start):
    if len(list) == M:
        print(' '.join(map(str, list)))
        return

    for i in range(start, N+1):
        if i not in list:
            list.append(i)
            dfs(i+1)
            list.pop()
dfs(1)