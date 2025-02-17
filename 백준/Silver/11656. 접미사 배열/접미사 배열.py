s = input()
suffixes = []
for i in range(len(s)):
    suffixes.append(s[i:])
suffixes.sort()
for suffix in suffixes:
    print(suffix)