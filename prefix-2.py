#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
  s = "mont"

i = 0
while i < len(a) and s[:len(s)] != a[i][:len(s)]:
  i = i + 1

if i < len(a):
  print(a[i])
