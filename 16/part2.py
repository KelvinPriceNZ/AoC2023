#!/usr/bin/env python3.12

import os
import sys
from dataclasses import dataclass
from collections import deque

@dataclass
class Cell:
   row: int
   col: int
   char: str
   energised: dict

   def __init__(self, row, col, char):
      self.row = row
      self.col = col
      self.char = char
      self.energised = {
         "right": 0,
         "up": 0,
         "left": 0,
         "down": 0,
      }


def change_dir(direction, change):
   new_dir = directions[change]
   new_v = direction[0] + new_dir[0]
   new_h = direction[1] + new_dir[1]
   return (new_v, new_h)


def draw_grid(grid):
   h = len(grid)
   w = len(grid[0])
   for r in range(h):
      for c in range(w):
         cell = grid[r][c]
         ch = cell.char
         for d in [ "right", "left", "up", "down" ]:
            if grid[r][c].energised[d] > 0:
               ch = f"\033[34m{ch}\033[0m"
               break
         print(ch, end='')
      print()
   print()


# ( change in height, change in width )
directions = {
   "up": (-1,0),
   "down": (1,0),
   "left": (0,-1),
   "right": (0,1),
   "up+right": (-1,1),
   "up+left": (-1,-1),
   "down+right": (1,1),
   "down+left": (1,-1),
}

BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

height = len(lines)
width = len(lines[0])

grid = [[ None for x in range(width)] for y in range(height)]

for r, line in enumerate(lines):
   for c, ch in enumerate(line):
      cell = Cell(r, c, ch)
      grid[r][c] = cell

best = 0

search_starts = deque()

for r in [0, height - 1]:
   for c in range(width):
      search_starts.append((r,c))

for c in [0, width - 1]:
   for r in range(height):
      search_starts.append((r,c))

while len(search_starts) > 0:
   for r in range(height):
      for c in range(width):
         grid[r][c].energised["right"] = 0
         grid[r][c].energised["left"] = 0
         grid[r][c].energised["up"] = 0
         grid[r][c].energised["down"] = 0
   s_row, s_col = search_starts.pop()
   start = grid[s_row][s_col]
   direction = directions["right"]
   queue = deque()

   queue.append((start, direction))

   #draw_grid(grid)

   cycle = 0
   while len(queue) > 0:
      cycle += 1
      step = queue.popleft()
      cell, direction = step
      r, c = cell.row, cell.col
      xy = (r, c)
      ch = cell.char
      if directions["right"] == direction:
         if grid[r][c].energised["right"] > 0: continue
      if directions["up"] == direction:
         if grid[r][c].energised["up"] > 0: continue
      if directions["left"] == direction:
         if grid[r][c].energised["left"] > 0: continue
      if directions["down"] == direction:
         if grid[r][c].energised["down"] > 0: continue

      if directions["right"] == direction: grid[r][c].energised["right"] += 1
      if directions["up"] == direction: grid[r][c].energised["up"] += 1
      if directions["left"] == direction: grid[r][c].energised["left"] += 1
      if directions["down"] == direction: grid[r][c].energised["down"] += 1
      if ch == '.':
         # Keep going
         if directions["right"] == direction:
            r, c = change_dir(xy, "right")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["right"]))
         if directions["left"] == direction:
            r, c = change_dir(xy, "left")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["left"]))
         if directions["up"] == direction:
            r, c = change_dir(xy, "up")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["up"]))
         if directions["down"] == direction:
            r, c = change_dir(xy, "down")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["down"]))
      if ch == '/':
         if directions["right"] == direction:
            r, c = change_dir(xy, "up")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["up"]))
         if directions["left"] == direction:
            r, c = change_dir(xy, "down")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["down"]))
         if directions["up"] == direction:
            r, c = change_dir(xy, "right")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["right"]))
         if directions["down"] == direction:
            r, c = change_dir(xy, "left")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["left"]))
      if ch == '\\':
         if directions["right"] == direction:
            r, c = change_dir(xy, "down")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["down"]))
         if directions["left"] == direction:
            r, c = change_dir(xy, "up")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["up"]))
         if directions["up"] == direction:
            r, c = change_dir(xy, "left")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["left"]))
         if directions["down"] == direction:
            r, c = change_dir(xy, "right")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["right"]))
      if ch == '|':
         if directions["right"] == direction or directions["left"] == direction:
            r, c = change_dir(xy, "up")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["up"]))
            r, c = change_dir(xy, "down")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["down"]))
         if directions["up"] == direction:
            r, c = change_dir(xy, "up")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["up"]))
         if directions["down"] == direction:
            r, c = change_dir(xy, "down")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["down"]))
      if ch == '-':
         if directions["down"] == direction or directions["up"] == direction:
            r, c = change_dir(xy, "left")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["left"]))
            r, c = change_dir(xy, "right")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["right"]))
         if directions["left"] == direction:
            r, c = change_dir(xy, "left")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["left"]))
         if directions["right"] == direction:
            r, c = change_dir(xy, "right")
            if height > r >= 0 and width > c >= 0:
               queue.append((grid[r][c], directions["right"]))

   total = 0
   for row in range(height):
      for col in range(width):
         for d in [ "right", "left", "up", "down" ]:
            if grid[row][col].energised[d] > 0:
               total += 1
               break

   best = max(best, total)
   #print(f"Total: {total}")

draw_grid(grid)

print(f"Best: {best}")
