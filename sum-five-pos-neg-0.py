#!/usr/bin/env python3

i = 0
totalp = 0
totaln = 0
num = int(input())

while num != 0:
  if num < 0:
    totaln = totaln + num
    num = int(input())
    i = i + 1
  else:
    totalp = totalp + num
    num = int(input())
    i = i + 1

print(totaln, totalp)
