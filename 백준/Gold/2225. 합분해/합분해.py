import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(K+1):
    dp[0][i] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % 1000000000

print(dp[N][K])