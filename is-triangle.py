#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("yes")

else:
    print("no")
