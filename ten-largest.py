#!/usr/bin/env python3

largest = 0
i = 0

while i < 10 - 1:
    v = int(input())
    if largest < v:
      largest = v
    i = i + 1

print(largest)
