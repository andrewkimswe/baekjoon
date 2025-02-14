import sys

data = list(map(int, sys.stdin.read().split()))
k = data[1]
numbers = data[2:]

numbers.sort()

sys.stdout.write(str(numbers[k-1]))