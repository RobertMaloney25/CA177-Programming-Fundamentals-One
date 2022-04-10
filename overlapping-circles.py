#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())

x2 = int(input())
y2 = int(input())
r2 = int(input())

cen = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

rad = (r1 + r2) * (r1 + r2)


if (cen == rad):
    print("no")
elif (cen > rad):
    print("no")
else:
    print("yes")
