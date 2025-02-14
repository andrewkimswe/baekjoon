import sys

read_line = sys.stdin.readline

total_cards = int(read_line())

cards = [int(read_line()) for _ in range(total_cards)]

cards.sort()

max_count = 1
current_count = 1
most_frequent = cards[0]

for i in range(1, total_cards):
    if cards[i] == cards[i - 1]:
        current_count += 1
    else:
        current_count = 1
    
    if current_count > max_count:
        max_count = current_count
        most_frequent = cards[i]

sys.stdout.write(str(most_frequent))