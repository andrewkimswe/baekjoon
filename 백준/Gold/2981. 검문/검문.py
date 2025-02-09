import sys
import math

n = int(sys.stdin.readline().strip())
numbers = sorted(int(sys.stdin.readline()) for _ in range(n))

gcd_val = numbers[1] - numbers[0]
for i in range(2, n):
    gcd_val = math.gcd(gcd_val, numbers[i] - numbers[i - 1])

result = set()
for i in range(2, int(gcd_val**0.5) + 1):
    if gcd_val % i == 0:
        result.add(i)
        result.add(gcd_val // i)

result.add(gcd_val)
print(*sorted(result))