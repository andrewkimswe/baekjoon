n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_avg = sum(score / max_score * 100 for score in scores) / n
print(new_avg)