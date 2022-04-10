#!/usr/bin/env python3

side = int(input())
rad = int(input())

carea = (3.14 * rad ** 2)
sarea = (side * side)

if carea > sarea:
   print("circle")

elif sarea > carea:
   print("square")

elif sarea == carea:
   print("same")
