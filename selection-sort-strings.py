#!/usr/bin/env python3

a = []

s = input()
while s != "end":
  a.append(s)
  s = input()

j = 0
while j < len(a):
  p = j
  k = j + 1
  while k < len(a):
    if a[k] < a[p]:
      p = k
    k = k + 1

  tmp = a[p]
  a[p] = a[j]
  a[j] = tmp
  j = j + 1

i = 0
while i < len(a):
  print(a[i])
  i = i + 1
