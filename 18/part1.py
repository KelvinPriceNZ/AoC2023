#!/usr/bin/env python3.12

import os
import sys
from dataclasses import dataclass
from collections import deque


@dataclass
class Cell:
   row: int
   col: int
   rgb: str
   direction: str
   distance: int

   def __init__(self,r,c,h,d,a):
      self.row = r
      self.col = c
      self.rgb = h
      self.direction = d
      self.distance = a


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

row = 0
col = 0
minr = maxr = minc = maxc = 0
cells = list()

for line in lines:
   minr = min(row, minr)
   maxr = max(row, maxr)
   minc = min(col, minc)
   maxc = max(col, maxc)
   direction, distance, colour = line.split(' ')
   cell = Cell(row, col, colour, direction, int(distance))
   cells.append(cell)
   if direction == 'R': col += int(distance)
   if direction == 'L': col -= int(distance)
   if direction == 'D': row += int(distance)
   if direction == 'U': row -= int(distance)

#print(f"{minr},{minc} {maxr},{maxc}")

r_offset = 0 - minr
c_offset = 0 - minc

minr = maxr = minc = maxc = 0
for i in range(len(cells)):
   cells[i].row += r_offset
   cells[i].col += c_offset
   row = cells[i].row
   col = cells[i].col
   minr = min(row, minr)
   maxr = max(row, maxr)
   minc = min(col, minc)
   maxc = max(col, maxc)

grid = [['.' for c in range(maxc + 1)] for r in range(maxr + 1) ]

height = len(grid)
width = len(grid[0])

#for row in range(height):
#   for col in range(width):
#      print(grid[row][col], end='')
#   print()

#print(f"{minr},{minc} {maxr},{maxc}")
for i in range(len(cells)):
   cell = cells[i]
   grid[cell.row][cell.col] = '#'

   if cell.direction == 'R':
      for c in range(cell.col, cell.col + cell.distance + 1):
         grid[cell.row][c] = '#'
   if cell.direction == 'L':
      for c in range(cell.col, cell.col - cell.distance - 1, -1):
         grid[cell.row][c] = '#'
   if cell.direction == 'D':
      for r in range(cell.row, cell.row + cell.distance + 1):
         grid[r][cell.col] = '#'
   if cell.direction == 'U':
      for r in range(cell.row, cell.row - cell.distance - 1, -1):
         grid[r][cell.col] = '#'

#for row in range(height):
#   for col in range(width):
#      print(grid[row][col], end='')
#   print()

border = 0
fcol = 0
for col in range(width):
   if grid[1][col] == '#': border = 1
   if border == 1 and grid[1][col] == '.': fcol = col; break

q = deque()

q.append((1,fcol))

while len(q) > 0:
   row, col = q.popleft()
   if grid[row][col] == '.': grid[row][col] = '#'
   for r in [ row - 1, row, row + 1 ]:
      for c in [ col - 1, col, col + 1 ]:
         if height > r >= 0 and width > c >= 0:
            if grid[r][c] == '.':
               p = (r,c)
               #if q.count(p) < 1:
               if p not in q:
                  q.append((r,c))

blocks = 0
for row in range(height):
   for col in range(width):
      ch = grid[row][col]
      if ch == '#': blocks += 1
#      print(ch, end='')
#   print()

print(blocks)
