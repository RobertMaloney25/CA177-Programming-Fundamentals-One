#!/usr/bin/env python3

if __name__ == "__main__":
  a = [6, 2, 3, 4, 5, 1]

i = 0
j = len(a) - 1

tmp = a[i]
a[i] = a[j]
a[j] = tmp
