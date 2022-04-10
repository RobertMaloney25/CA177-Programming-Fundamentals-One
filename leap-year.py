#!/usr/bin/env python3

year = int(input())

if (year % 4 == 0) and (year % 100 != 0):
    print("True")

elif (year % 400 == 0):
    print("True")

else:
    print("False")
