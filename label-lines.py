#!/usr/bin/env python3

a = []
n = 0

s = input()
while s != "end":
  a.append(s)
  s = input()
  n = n + 1

i = 0
while i < len(a):
  if 0 < len(a):
    print(i, n, a[i])
    i = i + 1
