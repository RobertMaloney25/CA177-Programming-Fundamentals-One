#!/usr/bin/env python3


mark = int(input())

first = 70
second = 50
third = 40

if mark >= first:
    print("first: True")
    print("second: False")
    print("third: False")
    print("fail: False")

if mark < first and mark >= second:
    print("first: False")
    print("second: True")
    print("third: False")
    print("fail: False")

if mark < second and mark >= third:
    print("first: False")
    print("second: False")
    print("third: True")
    print("fail: False")

if mark < third:
    print("first: False")
    print("second: False")
    print("third: False")
    print("fail: True")
