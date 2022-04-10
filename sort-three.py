#!/usr/bin/env python3

a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

i = 0
j = 1
if a[j] < a[i]:
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

i = 0
j = 2
if a[j] < a[i]:
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

i = 1
j = 2
if a[j] < a[i]:
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

print(a[0])
print(a[1])
print(a[2])
