N = int(input())

if N % 2 == 1:
    print(0)
    exit()

dp = [0] * (N+1)
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 
    for j in range(4, i, 2):
        dp[i] += dp[i-j] * 2
    dp[i] += 2

print(dp[N])