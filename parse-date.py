#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != " ":
  i = i + 1
day = s[:i]

if i < len(s):
  while i < len(s) and not("0" <= s[i] <= "9"):
    i = i + 1

if i < len(s):
  j = i
  while j < len(s) and s[j] != " ":
    j = j + 1
date = s[i:j]

if j < len(s):
  i = j
  while i < len(s) and s[i] == " ":
    i = i + 1

if i < len(s):
  j = i
  while j < len(s) and s[j] != ",":
    j = j + 1
month = s[i:j]

if j < len(s):
  i = j
  while i < len(s) and not("0" <= s[i] and s[i] <= "9"):
    i = i + 1

if i < len(s):
  j = i
  while j < len(s):
    j = j + 1
year = s[i:j]

print(month + " " + date + ", " + year + " (" + day + ")")
