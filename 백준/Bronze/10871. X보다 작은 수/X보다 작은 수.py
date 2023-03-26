N, X = map(int, input().split())
A = list(map(int, input().split()))
print(*[num for num in A if num < X])