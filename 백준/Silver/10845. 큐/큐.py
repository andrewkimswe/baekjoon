import sys
from collections import deque

input = sys.stdin.read
commands = input().split("\n")

queue = deque()
result = []

for command in commands:
    if not command:
        continue
    if command.startswith("push"):
        _, x = command.split()
        queue.append(int(x))
    elif command == "pop":
        result.append(queue.popleft() if queue else -1)
    elif command == "size":
        result.append(len(queue))
    elif command == "empty":
        result.append(1 if not queue else 0)
    elif command == "front":
        result.append(queue[0] if queue else -1)
    elif command == "back":
        result.append(queue[-1] if queue else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")