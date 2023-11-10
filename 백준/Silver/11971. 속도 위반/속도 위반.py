import sys

N, M = map(int, sys.stdin.readline().split())

limit_speeds = [0] * 1001
section_start = 0

for _ in range(N):
    length, limit_speed = map(int, sys.stdin.readline().split())
    for i in range(section_start, section_start + length):
        limit_speeds[i] = limit_speed
    section_start += length

driving_speeds = [0] * 1001
section_start = 0

for _ in range(M):
    length, driving_speed = map(int, sys.stdin.readline().split())
    for i in range(section_start, section_start + length):
        driving_speeds[i] = driving_speed
    section_start += length

max_violation = 0
for i in range(1001):
    if driving_speeds[i] > limit_speeds[i]:
        max_violation = max(max_violation, driving_speeds[i] - limit_speeds[i])

print(max_violation)
