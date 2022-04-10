#!/usr/bin/env python3

a = []
s = input()

while s != "end":
  a.append(int(s))
  s = input()

m = int(input())

i = 0
while i < len(a):
  print(a[i] + m)
  i = i + 1
