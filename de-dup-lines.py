#!/usr/bin/env python3

a = []
s = input()

while s != "end":

  i = 0
  while i < len(a) and s != a[i]:
    i = i + 1

  if not (i < len(a)):
    print(s)
    a.append(s)

  s = input()
