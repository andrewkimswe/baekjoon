import sys

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    found = False
    for p in range(3, n // 2 + 1, 2):
        if is_prime[p] and is_prime[n - p]:
            print(f"{n} = {p} + {n - p}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")