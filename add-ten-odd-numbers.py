#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

third1 = ((a * (a % 2)) + (b * (b % 2)) + (c * (c % 2)) + (d * (d % 2)))
third2 = ((e * (e % 2)) + (f * (f % 2)) + (g * (g % 2)))
third3 = ((i * (i % 2)) + (j * (j % 2)) + (h * (h % 2)))

print(third1 + third2 + third3)
