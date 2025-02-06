import sys

def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k

    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)

    return result

while True:
    n, k = map(int, sys.stdin.readline().split())
    if n == 0 and k == 0:  # 종료 조건
        break
    print(binomial_coefficient(n, k))