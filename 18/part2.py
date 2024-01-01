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

      """
      Each hexadecimal code is six hexadecimal digits long.
      The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number.
      The last hexadecimal digit encodes the direction to dig:
      0 means R, 1 means D, 2 means L, and 3 means U.
      """
      hexval = self.rgb[2:-1]   #strip the '(#)'
      new_distance = hexval[:-1]
      new_direction = hexval[-1]
      if new_direction == '0': self.direction = "R"
      if new_direction == '1': self.direction = "D"
      if new_direction == '2': self.direction = "L"
      if new_direction == '3': self.direction = "U"

      self.distance = int(new_distance, 16)


def shoelace(points):
   #A function to apply the Shoelace algorithm
  numberOfVertices = len(points)
  sum1 = 0
  sum2 = 0

  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + points[i][0] *  points[i+1][1]
    sum2 = sum2 + points[i][1] *  points[i+1][0]

  #Add xn.y1
  sum1 = sum1 + vertices[numberOfVertices-1][0]*points[0][1]
  #Add x1.yn
  sum2 = sum2 + points[0][0]*vertices[numberOfVertices-1][1]

  area = abs(sum1 - sum2) / 2

  return area


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
   direction, distance, colour = line.split(' ')
   cell = Cell(row, col, colour, direction, int(distance))
   cells.append(cell)
   if cell.direction == 'R': col += cell.distance
   if cell.direction == 'L': col -= cell.distance
   if cell.direction == 'D': row += cell.distance
   if cell.direction == 'U': row -= cell.distance
   minr = min(row, minr)
   maxr = max(row, maxr)
   minc = min(col, minc)
   maxc = max(col, maxc)

#print(f"{minr},{minc} {maxr},{maxc}")

r_offset = 0 - minr
c_offset = 0 - minc

# Translate coordinates to grid 0,0 to max row, max column
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
#print(f"{minr},{minc} {maxr},{maxc}")

"""
roughly 10,000,000 x roughly 12,000,000 = roughly 120,000,000,000,000
clearly not feasible memory wise for part1 solution
also, roughly 150,000,000 cells just in all the ranges
so, also not feasible

can I calculate all the rectangles and sum the areas ?

if so, I need the beginning and end point of each "line"
"""

grid = list()

for i in range(len(cells)):
   cell = cells[i]

   p1 = ( cell.row, cell.col )

   if cell.direction == 'R':
      p2 = ( cell.row, cell.col + cell.distance )
   if cell.direction == 'L':
      p2 = ( cell.row, cell.col - cell.distance )
   if cell.direction == 'D':
      p2 = ( cell.row + cell.distance, cell.col )
   if cell.direction == 'U':
      p2 = ( cell.row - cell.distance, cell.col )

   grid.append((p1,p2))

"""
ok, so now, grid is a list of lines with their beginning and end points
"""

# Get list of vertices
vertices = [ v[0] for v in grid ]

# Use shoelace algorithm to calculate polygon area
area = shoelace(vertices)

border = sum([ p.distance for p in cells ])
print(int(1 + area + border / 2))
