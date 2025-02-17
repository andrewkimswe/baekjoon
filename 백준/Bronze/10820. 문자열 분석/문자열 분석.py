import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    
    lower = sum(c.islower() for c in line)
    upper = sum(c.isupper() for c in line)
    digit = sum(c.isdigit() for c in line)
    space = sum(c.isspace() for c in line)
    
    print(lower, upper, digit, space)