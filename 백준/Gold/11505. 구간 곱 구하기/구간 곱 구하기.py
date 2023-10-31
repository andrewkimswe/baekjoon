import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)) % MOD
    return tree[node]

def update(node, start, end, index, value):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = value
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (update(node * 2, start, mid, index, value) * update(node * 2 + 1, mid + 1, end, index, value)) % MOD
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) * query(node * 2 + 1, mid + 1, end, left, right)) % MOD

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        nums[b] = c
        update(1, 0, N - 1, b, c)
    else:
        print(query(1, 0, N - 1, b - 1, c - 1))
