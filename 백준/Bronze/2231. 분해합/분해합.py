import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    s = sum((map(int, str(i))))
    disassemble = i + s
    if disassemble == N:
        print(i)
        break
    if i == N:
        print(0)