#!/usr/bin/env python3

n = int(input())
i = 0
a = []

while n != 0:
  if n < 0:
    a.append(int(n))
  else:
    print(n)
  n = int(input())

j = 0
while j < len(a):
  print(a[j])
  j = j + 1
