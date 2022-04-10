#!/usr/bin/env python3

n = int(input())
previous = 0
current = 1

i = 0
while i < n:
   print(previous)
   tmp = previous + current
   previous = current
   current = tmp
   i = i + 1
