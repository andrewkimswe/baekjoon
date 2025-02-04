import math

n = int(input())
A = math.prod(map(int, input().split()))

m = int(input())
B = math.prod(map(int, input().split()))

print(str(math.gcd(A, B))[-9:])