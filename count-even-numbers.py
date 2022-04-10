#!/usr/bin/env python3

n = int(input())
i = 0

while n != 0:
  if n % 2 == 0:
    i = i + 1
  n = int(input())

print(i)
