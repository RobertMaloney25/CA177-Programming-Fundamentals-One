#!/usr/bin/env python3

num = int(input())
string = str(num)
x = 0
i = 0
total = 0

while i < len(string):
    x = string[i]
    y = int(x)
    total = total + y
    i = i + 1

print(total)
