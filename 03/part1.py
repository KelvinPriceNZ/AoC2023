#!/usr/bin/env python3.12

import os
import sys
import re


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

height = len(lines)
width = len(lines[0])

part_numbers = list()
coords = list ()
for row, line in enumerate(lines):
   for col, _ in enumerate(line):
      if lines[row][col] not in '.0123456789':
         # keep co-ordinate tuples of symbols
         coords.append((row, col))

for i, line in enumerate(lines):
   # find a number
   p = 0
   while True:
      while p < width and line[p] not in '01234567890':
         p = p + 1

      if p == width:
         break

      m = re.match(r'(\d+)', line[p:])
      number = int(m.group(1))
      #print(f"Number {i}:{p} {number}", end='')

      l = len(m.group(1))

      for y in [ i - 1, i, i + 1 ]:
         if y < 0 or y >= height: continue
         for x in range(p-1, p+l+1):
            if x < 0 or x >= width: continue
            #print(f" {x}:{y} {lines[y][x]}", end='')
            if (y,x) in coords:
               part_numbers.append(number)

      p = p + l
      #print()

print(sum(part_numbers))
