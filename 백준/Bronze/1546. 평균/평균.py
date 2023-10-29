import sys
input = sys.stdin.readline

n = int(input())

originalList = list(map(int, input().split()))
maxScore = max(originalList)

newScoreList = []
for score in originalList:
    newScoreList.append(score/maxScore*100)
avg = sum(newScoreList)/n
print(avg)