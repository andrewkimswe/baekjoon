import sys

n = int(sys.stdin.readline().strip())
members = [tuple(sys.stdin.readline().split()) for _ in range(n)]

members.sort(key=lambda x: int(x[0]))

sys.stdout.write("\n".join(f"{age} {name}" for age, name in members) + "\n")