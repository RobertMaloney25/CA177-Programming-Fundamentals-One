#!/usr/bin/env python3

s = input()
t = ""
i = 0


last = s[len(s) - 1]
mid = s[1:len(s) - 1]
start = s[0]

print(last + mid + start)
