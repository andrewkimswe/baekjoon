import sys
input = sys.stdin.readline

N = int(input())
A = set(input().split())
M = int(input())
B = list(input().split())

for num in B:
    if num in A:
        print(1)
    else:
        print(0)
