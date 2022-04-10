#!/usr/bin/env python3

n = int(input())
i = 0

while n != 0:
  m = n + 1
  n = m % 2
  i = i + n
  n = int(input())

print(i)
