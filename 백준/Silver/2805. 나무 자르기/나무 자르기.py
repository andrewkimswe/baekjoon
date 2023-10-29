import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)

result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum([tree - mid for tree in trees if tree > mid])
    
    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
