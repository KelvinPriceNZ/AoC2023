#!/usr/bin/env python3.12

import os
import sys
import re


def next_in_pattern(p):
   t = zip(p[:-1], p[1:])
   s = list(map(lambda x: x[1] - x[0], t))

   if sum(s) == 0:
      s.insert(0, 0)
      return s

#   print(f"P: {p} {len(p)}")
#   print(f"S: {s} {len(s)}")

   n = next_in_pattern(s)
#   print(f"N: {n} {len(n)}")

   p.insert(0, p[0] - s[0])

   return p


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

sequences = list()
for line in lines:
   sequence = list(map(int, re.split(r'\s+', line)))
   sequences.append(sequence)

nums = list()

for s in sequences:
#   print(s)
   a = next_in_pattern(s)
   nums.append(a[0])
#   print(s)
#   print(a)

#print(nums)
print(sum(nums))
