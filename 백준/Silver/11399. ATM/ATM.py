N = int(input())
people = list(map(int, input().split()))

people.sort()
answer = 0

for x in range(1,N+1):
    answer += sum(people[0:x])
print(answer)