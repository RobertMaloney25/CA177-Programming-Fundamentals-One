#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
i = 0

while i < n:
  spaces = ""
  asterisks = ""

  if i < n // 2:
    spaces = ((n // 2) - i) * " "
    asterisks = ((2 * i) + 1) * "*"
    print(spaces + asterisks)

  elif i > n // 2:
    spaces = (i - n // 2) * " "
    asterisks = (2 * (n - i) - 1) * "*"
    print(spaces + asterisks)

  else:
    print("*" * n)
  i = i + 1
