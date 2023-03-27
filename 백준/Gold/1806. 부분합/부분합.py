import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 0
sum = 0
min_len = sys.maxsize

while True:
    if sum >= S:
        min_len = min(min_len, r - l)
        sum -= nums[l]
        l += 1
    elif r == N:
        break
    else:
        sum += nums[r]
        r += 1

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)