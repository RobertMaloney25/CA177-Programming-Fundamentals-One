#!/usr/bin/env python3

a = []
n = int(input())
i = 0

while n != 0:
  a.append(n)
  n = int(input())

smallest = a[0]
while i < len(a):
  if smallest > a[i]:
    smallest = a[i]
  i = i + 1

print(smallest)
