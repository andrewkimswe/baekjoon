import sys

n = int(sys.stdin.readline().strip())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

area = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += (x1 * y2) - (x2 * y1)

print(round(abs(area) / 2, 1))