#!/usr/bin/env python3

total = 0
num = int(input())

while num != 0:
  if num < 0:
    num = num * -1
    total = total + num
    num = int(input())
  else:
    total = total + num
    num = int(input())

print(total)
