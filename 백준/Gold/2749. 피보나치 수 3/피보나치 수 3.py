N = int(input())

MOD = 1000000
PISANO = 1500000
fib = [0, 1]

for i in range(2, PISANO):
    fib.append((fib[i-1] + fib[i-2]) % MOD)
    if fib[i] == 1 and fib[i-1] == 0:
        break

print(fib[N % PISANO])