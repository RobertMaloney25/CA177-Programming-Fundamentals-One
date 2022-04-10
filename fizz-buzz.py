#!/usr/bin/env python3

n = int(input())

i = 1
while i <= n:
  if i % 5 == 0 and i % 3 == 0:
    print("fizz-buzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buzz")
  else:
    print(i)
  i = i + 1
