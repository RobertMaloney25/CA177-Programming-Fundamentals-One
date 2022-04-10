#!/usr/bin/env python3

i = 0
n = int(input())
str = str(n)

while i < len(str):
    num = str[i]
    num = int(num)
    print("*" * num)
    i = i + 1
