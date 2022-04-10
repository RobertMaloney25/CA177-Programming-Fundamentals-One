#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
    i = i + 1

j = i
if i < len(s):
  while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
    j = j + 1
  print(s[i:j], len(s[:i]))
