#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
    i = i + 1

j = i
if i < len(s):
  while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
    j = j + 1
  print(s[i:j], len(s[:i]))
