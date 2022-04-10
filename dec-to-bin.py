#!/usr/bin/env python3

base = 2
s = ""

n = int(input())

while 0 < n:
  d = n % base
  s = str(d) + s
  n = n // base
print(s)
