import sys
input = sys.stdin.readline

N = int(input())
numbers = map(int, input().split())

count = 0

for n in numbers:
  for m in range(2, n+1):
    if n % m == 0:
      if n == m:
        count += 1
      break
      
print(count)