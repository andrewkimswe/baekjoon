import sys

t = int(sys.stdin.readline())
dp = [0] * 101

dp[1] = dp[2] = dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])