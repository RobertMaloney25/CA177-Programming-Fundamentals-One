#!/usr/bin/env python3

s = input()
i = 0
j = 0
tmp = 0
joe = 0

while joe == 0:
  if s == "":
    joe = 1

  while i < len(s):
    if s[i] != " ":
      tmp = i
      j = i
      i = len(s)
    i = i + 1

  k = 0
  while j < len(s):
    if s[j] == " ":
      k = j
      j = len(s)
    j = j + 1
    joe = 1
  print(s[tmp:k])
