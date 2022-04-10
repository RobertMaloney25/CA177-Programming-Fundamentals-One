#!/usr/bin/env python3

s = input()
i = 0

while i < (len(s) // 2) and s[i] == s[-i - 1]:
    i = i + 1

if i == (len(s) // 2):
  print("palindrome")
