try:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if ccw > 0:
        print(1)
    elif ccw < 0:
        print(-1)
    else:
        print(0)
except:
    exit()