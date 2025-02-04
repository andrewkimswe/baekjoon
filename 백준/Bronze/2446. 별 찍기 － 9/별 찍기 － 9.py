n = int(input())

# 위쪽 부분 (감소)
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아래쪽 부분 (증가)
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))