#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (s[i] < "0" or "9" < s[i]):
  i = i + 1

if i < len(s):
  j = i

  while j < len(s) and not (s[j] < "0" or "9" < s[j]):
    j = j + 1

if i < len(s):
  k = j

  while k < len(s) and (s[k] < "0" or "9" < s[k]):
    k = k + 1

if i < len(s):
  x = k

  while x < len(s) and not (s[x] < "0" or "9" < s[x]):
    x = x + 1

  print(s[k:x], k)
