crossing = input().strip()

positions = {}

for i, char in enumerate(crossing):
    if char in positions:
        positions[char].append(i)
    else:
        positions[char] = [i]
        
crossing_pairs = 0

for i in positions.values():
    start, end = i
    for j in positions.values():
        if j == i:
            continue
        if start < j[0] < end and end < j[1]:
            crossing_pairs += 1

print(crossing_pairs)
