import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)