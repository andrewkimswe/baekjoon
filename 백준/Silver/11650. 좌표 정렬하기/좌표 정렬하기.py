import sys
input = sys.stdin.readline

N = int(input())
coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

sorted_coordinates = sorted(coordinates)

for coord in sorted_coordinates:
    print(coord[0], coord[1])
