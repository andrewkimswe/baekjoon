import sys

input = sys.stdin.readline
mod = 1000000

s = input().strip()
n = len(s)

if s[0] == '0':
    print(0)
    exit()

dp = [0] * (n + 1)
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    one_digit = int(s[i-1])
    two_digit = int(s[i-2:i])

    if 1 <= one_digit <= 9:
        dp[i] = dp[i-1]

    if 10 <= two_digit <= 26:
        dp[i] = (dp[i] + dp[i-2]) % mod

print(dp[n])