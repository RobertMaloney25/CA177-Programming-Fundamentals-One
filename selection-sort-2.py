#!/usr/bin/env python3

a = []
s = input()

while s != "end":
  a.append(int(s))
  s = input()

i = int(input())

j = i
while i < len(a):
  if a[i] < a[j]:
    j = i
  i = i + 1
print(j)
