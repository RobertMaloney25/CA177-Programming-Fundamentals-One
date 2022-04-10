#!/usr/bin/env python3

i = 0
total = 0

while i < 5:
  num = int(input())
  if num < 0:
    num = num * -1
    total = total + num
  else:
    total = total + num
  i = i + 1

print(total)
