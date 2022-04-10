#!/usr/bin/env python3

bar = [0] * 10

s = input()
while s != "end":
  num = int(s)
  bar[num] = bar[num] + 1
  s = input()

i = 0
while i < 10:
  print(i, bar[i] * "*")
  i = i + 1
