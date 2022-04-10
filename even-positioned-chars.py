#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):
    if i % 2 == 0:
      string = str(s[i])
      t = t + string
    i = i + 1

print(t)
