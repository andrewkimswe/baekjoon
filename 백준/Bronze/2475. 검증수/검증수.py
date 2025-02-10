nums = list(map(int, input().split()))
print(sum(n ** 2 for n in nums) % 10)