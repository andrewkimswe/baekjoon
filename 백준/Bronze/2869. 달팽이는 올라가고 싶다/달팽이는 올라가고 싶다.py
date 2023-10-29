import math, sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

days = math.ceil((V - A) / (A - B) + 1)

print(days)