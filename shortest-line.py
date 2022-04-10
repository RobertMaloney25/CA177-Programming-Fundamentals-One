#!/usr/bin/env python3

s = input()
small = len(s)

while s != "end":
  if len(s) < small:
    small = len(s)
  s = input()

print(small)
