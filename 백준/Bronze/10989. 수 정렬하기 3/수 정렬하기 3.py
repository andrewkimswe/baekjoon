import sys

read_line = sys.stdin.readline

total_count = int(read_line())

frequency = [0] * 10001

for _ in range(total_count):
    value = int(read_line())
    frequency[value] += 1

for number in range(10001):
    if frequency[number] != 0:
        for _ in range(frequency[number]):
            print(number)