import sys
from collections import deque

input = sys.stdin.read
commands = input().split("\n")

n = int(commands[0])
dq = deque()
result = []

for i in range(1, n + 1):
    cmd = commands[i].split()

    if cmd[0] == "push_front":
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        dq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        result.append(str(dq.popleft()) if dq else "-1")
    elif cmd[0] == "pop_back":
        result.append(str(dq.pop()) if dq else "-1")
    elif cmd[0] == "size":
        result.append(str(len(dq)))
    elif cmd[0] == "empty":
        result.append("0" if dq else "1")
    elif cmd[0] == "front":
        result.append(str(dq[0]) if dq else "-1")
    elif cmd[0] == "back":
        result.append(str(dq[-1]) if dq else "-1")

sys.stdout.write("\n".join(result))