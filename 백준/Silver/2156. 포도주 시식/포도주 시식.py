import sys
input = sys.stdin.readline

N = int(input().strip())
wine = [0] + [int(input().strip()) for _ in range(N)]

if N == 1:
    print(wine[1])
    exit()

dp = [0] * (N + 1)
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[N])