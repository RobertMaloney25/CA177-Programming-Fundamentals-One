#!/usr/bin/env python3

i = 0
total = 0

while i < 10:
  num = int(input())

  if num > 0:
    total = total + num
  i = i + 1

print(total)
