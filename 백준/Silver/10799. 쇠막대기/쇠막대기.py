import sys

s = sys.stdin.readline().strip()
stack = []
pieces = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if s[i - 1] == "(":
            pieces += len(stack)
        else:
            pieces += 1

print(pieces)