#!/usr/bin/env python3

n = int(input())

if n % 2 == 0:
   n = n // 2
   print(n)

elif n % 2 != 0:
   n = (n * 3) + 1
   print(n)
