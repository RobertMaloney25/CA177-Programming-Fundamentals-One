#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
    if "a" <= s[i] and s[i] <= "g":
      print(s[i])
      i = len(s)
    else:
      i = i + 1
