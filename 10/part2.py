#!/usr/bin/env python3.12

import os
import sys
from dataclasses import dataclass
from collections import deque


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
   'S': '+',
}

@dataclass
class Cell:
   row: int
   col: int
   pipe: str
   exits: list
   connects: list
   visited: bool

   def __init__(self, row, col, pipe):
      self.row  = row
      self.col = col
      self.pipe = pipe
      self.exits = list()
      self.connects = list()
      self.visited = False


def floodfill(char, x, y, grid):
   q = deque()
   q.append((x,y))
   height = len(grid)
   width = len(grid[0])
   while len(q) > 0:
      r, c = q.popleft()
      grid[r][c].pipe = char
      for i in [ r - 1, r, r + 1]:
         if i < 0 or i >= height: continue
         for j in [ c - 1, c, c + 1]:
            if j < 0 or j >= width: continue
            if grid[i][j].pipe == ' ':
               q.append((i,j))


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

width = len(lines[0])
height = len(lines)

s_coord = ()

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

row = s_coord[0]
col = s_coord[1]
lines[row][col].pipe = 'S'
lines[row][col].connects = []
lines[row][col].exits = []
if 'S' in lines[row - 1][col].exits:
   lines[row][col].connects.append((row - 1, col))
   lines[row][col].exits.append("N")
if 'N' in lines[row + 1][col].exits:
   lines[row][col].connects.append((row + 1, col))
   lines[row][col].exits.append("S")
if 'E' in lines[row][col - 1].exits:
   lines[row][col].connects.append((row, col - 1))
   lines[row][col].exits.append("W")
if 'W' in lines[row][col + 1].exits:
   lines[row][col].connects.append((row, col + 1))
   lines[row][col].exits.append("E")

path = lines[s_coord[0]][s_coord[1]].connects.copy()
offset = 2

while True:
   n = path[-offset:]
   edges = []
   offset = 0
   for s in n:
      r = s[0]
      c = s[1]
      edges.extend(lines[r][c].connects)
   chg = False
   for edge in edges:
      if edge not in path:
         path.append(edge)
         offset += 1
         chg = True

   if not chg:
      break

# Print the cleaned up "map" of just pipes in the loop
for row in range(height):
   for col in range(width):
      if (row, col) not in path:
         lines[row][col].pipe = ' '
      print(graphic[lines[row][col].pipe], end='')
   print()

"""
Okay, we now have a "clean" map, what's inside the loop and what's outside ?

Let's follow along the loop, keep our left hand on the pipe

If we see a space on our right hand, floodfill with *
"""

x, y = s_coord
print(f"START {lines[x][y]}")
next = lines[x][y].connects[0]
while next != s_coord:
   x, y = next[0], next[1]
   lines[x][y].visited = True
   shape = lines[x][y].pipe
   ptr = ''
   for exit in lines[x][y].exits:
      if exit == "N": r, c = x - 1, y
      if exit == "S": r, c = x + 1, y
      if exit == "E": r, c = x, y + 1
      if exit == "W": r, c = x, y - 1
      if not lines[r][c].visited:
         #print(f"    {exit} {lines[r][c]}")
         next = (r,c)
         ptr = exit
   # What cell is on my 'right'
   if ptr == "N":
      if shape == "|": r, c = x, y + 1
      if shape == "J": r, c = x + 1, y
      if shape == "L": r, c = x - 1, y
   if ptr == "S":
      if shape == "|": r, c = x, y - 1
      if shape == "7": r, c = x + 1, y
      if shape == "F": r, c = x, y - 1
   if ptr == "E":
      if shape == "-": r, c = x + 1, y
      if shape == "L": r, c = x, y - 1
      if shape == "F": r, c = x, y + 1
   if ptr == "W":
      if shape == "-": r, c = x - 1, y
      if shape == "J": r, c = x, y - 1
      if shape == "7": r, c = x, y + 1
   # If the cell on my 'right' is empty, floodfill it
   if lines[r][c].pipe == ' ':
      q = deque()
      q.append((r,c))
      while len(q) > 0:
         r, c = q.popleft()
         if lines[r][c].pipe != ' ': continue
         lines[r][c].pipe = '*'
         found = False
         for i in [ r - 1, r, r + 1]:
            if i < 0 or i >= height: continue
            for j in [ c - 1, c, c + 1]:
               if j < 0 or j >= width: continue
               if lines[i][j].pipe == ' ':
                  found = True
                  q.append((i,j))
               if found: break
            if found: break

graphic['*'] = "\033[31m*\033[0m" # Red *
graphic[' '] = "\033[34m#\033[0m" # Blue #
graphic['S'] = "\033[32m+\033[0m" # Green +

stars = 0
blanks = 0
for row in range(height):
   for col in range(width):
      if lines[row][col].pipe == '*': stars += 1
      if lines[row][col].pipe == ' ': blanks += 1
      print(graphic[lines[row][col].pipe], end='')
   print()

print(f"Side {graphic['*']} {stars:5}")
print(f"Side {graphic[' ']} {blanks:5}")
print("""
The * are either inside or outside
the # is the opposite
Whatever colour/shape 0,0 is, is "outside"
So the answer is the count for the "inside" colour/shape
""")
