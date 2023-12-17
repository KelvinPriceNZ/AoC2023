#!/usr/bin/env python3.12

import os
import sys


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

total = 0
for line in lines:
   for code in line.split(","):
      hash_code = 0
      for c in code:
         hash_code += ord(c)
         hash_code *= 17
         hash_code %= 256
      total += hash_code

print(total)
