import sys

def solve(n, k):
    min_required = k * (k + 1) // 2

    if min_required > n:
        return -1
    elif (n - min_required) % k == 0:
        return k - 1
    else:
        return k

n, k = map(int, sys.stdin.readline().split())
print(solve(n, k))