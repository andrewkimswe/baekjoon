x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if y4 - y2 > 0 and y1 - y3 > 0:
  if x2 - x3 > 0 and x2 - x4 < 0:
    x2 = x3
  if x4 - x1 > 0 and x1 - x3 > 0:
    x1 = x4

if x4 - x2 > 0 and x1 - x3 > 0:
  if y2 - y3 > 0 and y2 - y4 < 0:
    y2 = y3
  if y4 - y1 > 0 and y1 - y3 > 0:
    y1 = y4

area = (x2-x1)*(y2-y1)
print(area)