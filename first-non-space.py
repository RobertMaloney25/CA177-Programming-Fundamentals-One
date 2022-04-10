#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and not (s[i] != " "):
    i = i + 1

if i < len(s):
  print(len(s[:i]))

else:
  print("-1")
