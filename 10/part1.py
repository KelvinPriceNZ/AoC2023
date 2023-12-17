#!/usr/bin/env python3.12

import os
import sys
from dataclasses import dataclass


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this
"""

lookup = {
   '|': [ 'N', 'S' ],
   '-': [ 'W', 'E' ],
   'L': [ 'N', 'E' ],
   'J': [ 'N', 'W' ],
   '7': [ 'S', 'W' ],
   'F': [ 'S', 'E' ],
   '.': [],
   ' ': [],
   'S': [ 'N', 'S', 'E', 'W' ],
}

graphic = {
   '|': '│',
   '-': '─',
   'L': '└',
   'J': '┘',
   '7': '┐',
   'F': '┌',
   '.': ' ',
   ' ': ' ',
   'S': '#',
}

@dataclass
class Cell:
   row: int
   col: int
   pipe: str
   exits: list
   connects: list

   def __init__(self, row, col, pipe):
      self.row  = row
      self.col = col
      self.pipe = pipe
      self.exits = list()
      self.connects = list()


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

width = len(lines[0])
height = len(lines)

s_coord = ()

# Prepare the "map"
for row in range(height):
   lines[row] = list(lines[row])
   line = lines[row]
   for col in range(width):
      if line[col] == 'S': s_coord = ( row, col )
      cell = Cell(row, col, line[col])
      lines[row][col] = cell
      lines[row][col].exits = lookup[cell.pipe]
      print(line[col].pipe, end='')
   print()

# Blank out any "map" grid cells that don't have both neccessary neighbours
for row in range(height):
   for col in range(width):
      if (row, col) != s_coord:
         for exit in lines[row][col].exits:
            if exit == 'N':
               north = row - 1
               if north >= 0:
                  if 'S' not in lines[north][col].exits:
                     lines[row][col].pipe = ' '
                     lines[row][col].exits = []
                  else:
                     lines[row][col].connects.append((north, col))
               elif row == 0:
                  lines[row][col].pipe = ' '
                  lines[row][col].exits = []
                  lines[row][col].connects = []
            if exit == 'S':
               south = row + 1
               if south < height:
                  if 'N' not in lines[south][col].exits:
                     lines[row][col].pipe = ' '
                     lines[row][col].exits = []
                  else:
                     lines[row][col].connects.append((south, col))
               elif south == height:
                  lines[row][col].pipe = ' '
                  lines[row][col].exits = []
                  lines[row][col].connects = []
            if exit == 'W':
               west = col - 1
               if west >= 0:
                  if 'E' not in lines[row][west].exits:
                     lines[row][col].pipe = ' '
                     lines[row][col].exits = []
                  else:
                     lines[row][col].connects.append((row, west))
               elif col == 0:
                  lines[row][col].pipe = ' '
                  lines[row][col].exits = []
                  lines[row][col].connects = []
            if exit == 'E':
               east = col + 1
               if east < width:
                  if 'W' not in lines[row][east].exits:
                     lines[row][col].pipe = ' '
                     lines[row][col].exits = []
                  else:
                     lines[row][col].connects.append((row, east))
               elif east == width:
                  lines[row][col].pipe = ' '
                  lines[row][col].exits = []
                  lines[row][col].connects = []
      print(graphic[lines[row][col].pipe], end='')
   print()

# Set up the satrt cell, follow the pipe loop in both directions until all pipes visited
row = s_coord[0]
col = s_coord[1]
lines[row][col].pipe = 'S'
lines[row][col].connects = []
if 'N' in lines[row - 1][col].exits: lines[row][col].connects.append((row - 1, col))
if 'S' in lines[row + 1][col].exits: lines[row][col].connects.append((row + 1, col))
if 'E' in lines[row][col - 1].exits: lines[row][col].connects.append((row, col - 1))
if 'W' in lines[row][col + 1].exits: lines[row][col].connects.append((row, col + 1))

path = lines[s_coord[0]][s_coord[1]].connects
offset = 2

while True:
   n = path[-offset:]
   edges = []
   offset = 0
   for s in n:
      r = s[0]
      c = s[1]
      for e in lines[r][c].connects:
         edges.append(e)
   chg = False
   for edge in edges:
      if edge not in path:
         path.append(edge)
         offset += 1
         chg = True

   if not chg:
      break

# Answer will be half of the pipe loop length
print(len(path))
print(len(path)//2)
