#!/usr/bin/env python3.12

import os
import sys
from itertools import combinations


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

for idx, line in enumerate(lines):
   print(line)
   lines[idx] = list(line)

height = len(lines)
width = len(lines[0])

print(f"{height} x {width}")
blanks = list()
for idx, row in enumerate(lines):
   if '#' not in row:
      #print("New row")
      blanks.append(idx)
for i in reversed(blanks):
   lines.insert(i, list('.' * width))

height = len(lines)

blanks = []
for w in range(width):
   #print( [ row[w] for row in lines] )
   if '#' not in [ row[w] for row in lines]:
      #print("New col")
      blanks.append(w)
for i in reversed(blanks):
   for r in range(height):
      lines[r].insert(i, '.')

width = len(lines[0])

for idx, line in enumerate(lines):
   print(''.join(line))

print(f"{height} x {width}")
coords = list()
for r in range(height):
   for c in range(width):
      if lines[r][c] == '#':
         coords.append((r,c))

print(len(coords))
nums = list()
for stars in combinations(coords,2):
   x1, y1 = stars[0]
   x2, y2 = stars[1]
   #print(f"{x1}:{y1} {x2}:{y2}")
   nums.append(abs(x1-x2) + abs(y1-y2))

print(sum(nums))
