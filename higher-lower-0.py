#!/usr/bin/env python3

num = int(input())

while num != 0:
  num2 = int(input())
  if num2 == 0:
    num = 0
  elif num2 > num:
    print("higher")
  elif num2 < num:
    print("lower")
  elif num2 == num:
    print("equal")
  num = num2
