import sys
left = list(input())
right = []
m = int(input())
for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])
print(''.join(left + right[::-1]))