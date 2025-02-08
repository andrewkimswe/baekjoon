import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[j] < A[i]:
            dec[i] = max(dec[i], dec[j] + 1)

result = max(inc[i] + dec[i] - 1 for i in range(N))
print(result)