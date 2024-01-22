def count_01(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    prev_0, prev_1 = 1, 0
    curr_0, curr_1 = 0, 1

    for _ in range(2, n + 1):
        curr_0, curr_1 = curr_0 + prev_0, curr_1 + prev_1
        prev_0, prev_1 = curr_0 - prev_0, curr_1 - prev_1

    return (curr_0, curr_1)

t = int(input())

for _ in range(t):
    n = int(input())
    zero_count, one_count = count_01(n)
    print(zero_count, one_count)
