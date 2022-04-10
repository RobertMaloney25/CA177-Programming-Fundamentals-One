#!/usr/bin/env python3

s = input()
while s != "end":
  i = 0
  empty = ""
  while i < len(s):
    if ("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z"):
      empty += s[i]
    i += 1
  print(empty)
  s = input()
