#!/usr/bin/env python3

n = 1
i = 0

while i < n:
   n = int(input())
   if n % 5 == 0 and n % 3 == 0:
      print(n)
      n = 0
      i = i + 1
