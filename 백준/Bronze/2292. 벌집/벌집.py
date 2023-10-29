import sys
input = sys.stdin.readline

N = int(input())
honeycombNumber = 1
count = 1

while N > honeycombNumber:
    honeycombNumber += 6 * count
    count += 1

print(count)