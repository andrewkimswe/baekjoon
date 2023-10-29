import sys
input = sys.stdin.readline

def is_vps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

T = int(input())

for _ in range(T):
    s = input().strip()
    print(is_vps(s))
