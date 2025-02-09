from itertools import combinations

n = int(input().strip())
nums = []

for length in range(1, 11):
    for comb in combinations(range(10), length):
        nums.append(int("".join(map(str, sorted(comb, reverse=True)))))

nums.sort()
print(nums[n] if n < len(nums) else -1)