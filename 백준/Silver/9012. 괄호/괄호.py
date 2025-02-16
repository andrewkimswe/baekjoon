import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    is_vps = True
    for char in sys.stdin.readline().strip():
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    print("YES" if is_vps and not stack else "NO")