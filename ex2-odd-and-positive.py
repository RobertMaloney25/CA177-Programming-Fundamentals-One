#!/usr/bin/env python3

n = input()

while n != "end":
  if int(n) % 2 == 1 and int(n) > 0:
    print(n)
  n = input()
