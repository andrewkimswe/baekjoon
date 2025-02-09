import sys

n, B, C = map(int, input().split())
a = list(map(int, input().split()))
cost = 0

# 예외 처리
if B <= C:
    print(sum(a) * B)
    sys.exit()

# 18185와 동일
for i in range(n - 2):
    if a[i + 1] > a[i + 2]:
        min_count = min(a[i], a[i + 1] - a[i + 2])
        cost += (B + C) * min_count
        a[i] -= min_count
        a[i + 1] -= min_count

    min_count = min(a[i], a[i + 1], a[i + 2])
    cost += (B + (2 * C)) * min_count
    a[i] -= min_count
    a[i + 1] -= min_count
    a[i + 2] -= min_count

for i in range(n - 1):
    min_count = min(a[i], a[i + 1])
    cost += (B + C) * min_count
    a[i] -= min_count
    a[i + 1] -= min_count

cost += (B * sum(a))

print(cost)