#!/usr/bin/env python3

small = int(input())
i = 0

while i < 10 - 1:
    total = int(input())
    if total > 0 and small > total:
      small = total
    i = i + 1

print(small)
