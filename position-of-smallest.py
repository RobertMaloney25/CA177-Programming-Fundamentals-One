#!/usr/bin/env python3

if __name__ == "__main__":
  a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

small = a[0]
i = 0
tmp = 0
while i < len(a):
  if small > a[i]:
    small = a[i]
    tmp = i
  i = i + 1

print(tmp)
