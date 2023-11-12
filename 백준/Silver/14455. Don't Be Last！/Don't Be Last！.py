from collections import defaultdict

cows = defaultdict(int)
names = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie',  'Henrietta']

for n in names:
    cows[n] = 0

N = int(input())

for _ in range(N):
    name, milk = input().split()
    cows[name] += int(milk)

cows_list = [[milk, cow] for cow, milk in cows.items()]
cows_list.sort()

result = 'Tie'
milk = cows_list[0][0]

i = 1
for i in range(1, 7):
    if cows_list[i][0] != milk:
        break

if i == 6 and cows_list[6][0] != milk:
    result = cows_list[6][1]

if i != 6 and cows_list[i][0] != cows_list[i+1][0]:
    result = cows_list[i][1]

print(result)