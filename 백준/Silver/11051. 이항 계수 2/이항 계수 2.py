import sys

MOD = 10007

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = dp[i][i] = 1

    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

print(dp[n][k])