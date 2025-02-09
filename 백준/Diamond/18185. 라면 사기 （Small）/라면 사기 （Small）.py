n = int(input())
a = list(map(int, input().split()))
cost = 0

# 3개 묶음 해결
for i in range(n - 2):
    if a[i + 1] > a[i + 2]: # 예외 처리
        min_count = min(a[i], a[i + 1] - a[i + 2])
        cost += 5 * min_count
        a[i] -= min_count
        a[i + 1] -= min_count

    min_count = min(a[i], a[i + 1], a[i + 2])
    cost += 7 * min_count
    a[i] -= min_count
    a[i + 1] -= min_count
    a[i + 2] -= min_count

# 2개 묶음 해결
for i in range(n - 1):
    min_count = min(a[i], a[i + 1])
    cost += 5 * min_count
    a[i] -= min_count
    a[i + 1] -= min_count

# 1개 묶음 해결
cost += (3 * sum(a))

print(cost)