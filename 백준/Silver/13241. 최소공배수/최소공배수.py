import sys
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

a, b = map(int, sys.stdin.readline().split())
print(lcm(a, b))