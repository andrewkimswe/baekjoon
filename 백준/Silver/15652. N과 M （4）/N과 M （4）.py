N, M = map(int, input().split())
list = []


def dfs(start):
  if len(list) == M:
    print(' '.join(map(str, list)))
    return

  for i in range(start, N + 1):
    list.append(i)
    dfs(i)
    list.pop()


dfs(1)