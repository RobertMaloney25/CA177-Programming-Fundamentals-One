#!/usr/bin/env python3

small = int(input())
i = 0

while i < 10 - 1:
    v = int(input())
    if small > v:
      small = v
    i = i + 1

print(small)
