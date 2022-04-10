#!/usr/bin/env python3

num = int(input())
i = 0

while i < 5:
  num2 = int(input())
  if num2 > num:
    print("higher")
  elif num2 < num:
    print("lower")
  elif num2 == num:
    print("equal")
  num = num2
  i = i + 1
