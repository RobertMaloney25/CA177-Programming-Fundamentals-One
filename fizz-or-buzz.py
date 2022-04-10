#!/usr/bin/env python3

num = int(input())

if num % 5 == 0 and num % 3 == 0:
    print("fizz-buzz")

elif num % 3 == 0:
    print("fizz")

elif num % 5 == 0:
    print("buzz")

else:
    print(num)
