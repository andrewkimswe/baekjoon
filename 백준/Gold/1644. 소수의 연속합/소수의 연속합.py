import math

N = int(input())
a = [False, False] + [True] * (N-1)
prime = []

for i in range(2, N+1):
  if a[i]:
    prime.append(i)
    for j in range(2*i,N+1,i):
      a[j] = False

answer = 0;
start = 0;
end = 0;

while end <= len(prime):
  temp = sum(prime[start:end])
  if temp == N:
    answer += 1
    end += 1
  elif temp < N:
    end += 1
  else:
    start += 1
print(answer)