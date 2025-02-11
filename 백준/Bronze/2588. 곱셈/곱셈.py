a = int(input())
b = input()

for digit in reversed(b):
    print(a * int(digit))

print(a * int(b))