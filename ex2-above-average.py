#!/usr/bin/env python3

n = int(input())
sum = 0
i = 0
a = []

while n != 0:
  a.append(n)
  n = int(input())
  i = i + 1

j = 0
while j < len(a):
  sum = sum + a[j]
  j = j + 1

avg = sum // j

k = 0
while k < len(a):
  if a[k] > avg:
    print(a[k])
  k = k + 1
