#!/usr/bin/env python3

i = 0
totalp = 0
totaln = 0

while i < 5:
  num = int(input())
  if num < 0:
    totaln = totaln + num
    i = i + 1
  else:
    totalp = totalp + num
    i = i + 1

print(totaln, totalp)
