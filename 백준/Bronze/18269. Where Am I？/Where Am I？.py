N = int(input())
mailboxes = input()

K = 1
while K < N:
    seen = set()
    all_unique = True
    for i in range(N-K+1):
        substring = mailboxes[i:i+K]
        if substring in seen:
            all_unique = False
            break
        seen.add(substring)
    if all_unique:
        N = K
    K += 1
print(N)