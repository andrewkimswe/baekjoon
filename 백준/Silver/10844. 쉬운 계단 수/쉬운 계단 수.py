import sys

MOD = 1000000000
n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1]
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] %= MOD

print(sum(dp[n]) % MOD)