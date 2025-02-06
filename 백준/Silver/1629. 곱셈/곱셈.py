import sys

def power_mod(a, b, c):
    if b == 0:
        return 1
    
    half = power_mod(a, b // 2, c)
    
    half = (half * half) % c

    if b % 2:
        half = (half * a) % c

    return half

a, b, c = map(int, sys.stdin.readline().split())
print(power_mod(a, b, c))