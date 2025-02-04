import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = int(sys.stdin.readline())

while True:
    if is_palindrome(n) and is_prime(n):
        print(n)
        break
    n += 1