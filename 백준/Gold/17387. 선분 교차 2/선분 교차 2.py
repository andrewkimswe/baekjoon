import sys

def ccw(x1, y1, x2, y2, x3, y3):
    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    return 0

def is_overlapping(x1, y1, x2, y2, x3, y3, x4, y4):
    return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
           min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

abc = ccw(x1, y1, x2, y2, x3, y3)
abd = ccw(x1, y1, x2, y2, x4, y4)
cda = ccw(x3, y3, x4, y4, x1, y1)
cdb = ccw(x3, y3, x4, y4, x2, y2)

if abc * abd <= 0 and cda * cdb <= 0:
    if abc == 0 and abd == 0 and cda == 0 and cdb == 0:
        if is_overlapping(x1, y1, x2, y2, x3, y3, x4, y4):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)