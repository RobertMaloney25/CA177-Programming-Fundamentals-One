#!/usr/bin/env python3

s = input()
n = 0
i = 0

while i < len(s):
   n = (2 * n) + int(s[i])
   i = i + 1

print(n)
