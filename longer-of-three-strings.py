#!/usr/bin/env python3

string1 = input()
string2 = input()
string3 = input()

len1 = len(string1)
len2 = len(string2)
len3 = len(string3)

if len1 < len2 > len3:
    print(string2)

elif len2 < len3 > len1:
    print(string3)

elif len3 < len1 > len2:
    print(string1)
