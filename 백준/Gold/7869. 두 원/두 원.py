import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d >= r1 + r2:
    print("0.000")
elif d <= abs(r1 - r2):
    print("{0:.3f}".format(math.pi * min(r1, r2)**2))
else:
    theta1 = math.acos((r1**2 + d**2 - r2**2) / (2 * r1 * d))
    theta2 = math.acos((r2**2 + d**2 - r1**2) / (2 * r2 * d))
    area1 = r1**2 * theta1 - r1**2 * math.sin(theta1) * math.cos(theta1)
    area2 = r2**2 * theta2 - r2**2 * math.sin(theta2) * math.cos(theta2)
    print("{0:.3f}".format(area1 + area2))