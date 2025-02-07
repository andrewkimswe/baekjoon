import sys

MAX = 123456 * 2
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

prime_count = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    print(prime_count[2 * n] - prime_count[n])