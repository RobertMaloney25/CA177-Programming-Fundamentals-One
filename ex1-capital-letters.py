#!/usr/bin/env python3


s = input()
i = 0

while i < len(s):
   if 0 < len(s):
      if "A" <= s[i] and s[i] <= "Z":
         print(s[i])
   i = i + 1
