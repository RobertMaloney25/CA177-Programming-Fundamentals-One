#!/usr/bin/env python3

hyp = input()
word = input()

i = 0
if len(word) == len(hyp):
  while i < len(word):
    if word[i] == hyp[i] or "-":
      i = i + 1
  print("yes")

else:
  print("no")
