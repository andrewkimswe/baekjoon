import sys
input = sys.stdin.readline

N = int(input())
count = 0

while N % 5 != 0 and N >= 0:
    N -= 3
    count += 1

if N < 0:
    print(-1)
else:
    count += N // 5
    print(count)