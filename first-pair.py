#!/usr/bin/env python3

s = input()

i = 1
while i < len(s) and (s[i] != s[i - 1]):
  i = i + 1

if i < len(s):
  print(s[i] * 2)
