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
   lines[idx] = list(line)
   print(line)

height = len(lines)
width = len(lines[0])
print(f"{height} x {width}")

"""
Create a matrix that matches the star map
Fill it with the value 1
Then for expansion, change 1 to the expansion rate
Then later when calculating the Manhattan distance, use the value in the matrix cell
"""

#print(lines)
matrix = [[ 1 for r in range(height)] for c in range(width)]
#print(matrix)

# 2 for part 1, 1,000,000 for part 2
expansion_rate = 1_000_000

blanks = list()
for idx, row in enumerate(lines):
   if '#' not in row:
      #print("New row")
      matrix[idx] = [ expansion_rate for x in range(width) ]
for w in range(width):
   #print( [ row[w] for row in lines] )
   if '#' not in [ row[w] for row in lines]:
      #print("New col")
      for row in range(height):
         matrix[row][w] = expansion_rate
#print("===")
#print(matrix)

coords = list()
for r in range(height):
   for c in range(width):
      if lines[r][c] == '#':
         coords.append((r,c))

print(len(coords))
nums = list()
for stars in combinations(coords,2):
   r1, c1 = stars[0]
   r2, c2 = stars[1]
   #print(f"{r1}:{c1} {r2}:{c2}")
   x = 0
   for d in range(min(r1,r2), max(r1,r2)):
      x += matrix[d][c1]
   y = 0
   for d in range(min(c1,c2), max(c1,c2)):
      y += matrix[r1][d]
   dist = x + y
   nums.append(dist)

print(sum(nums))
