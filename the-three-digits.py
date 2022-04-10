#!/usr/bin/env python3

num = int(input())

print((num - num % 100) // 100)
print((num % 100 - num % 10) // 10)
print(num % 10)
