import sys

n = int(sys.stdin.readline())
stairs = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * (n + 1)

if n == 1:
    print(stairs[1])
    exit()
elif n == 2:
    print(stairs[1] + stairs[2])
    exit()

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[n])