#!/usr/bin/env python3.12

import os
import sys


def compare(left, right):
   diffs = 0
   for i in range(len(left)):
      for pair in zip(left[i], right[i]):
         if pair[0] != pair[1]:
            diffs += 1
   return diffs

def find_mirror_line(area_map):
   row = -1
   for n in range(len(area_map)):
      if n == 0: continue
      size = len(area_map)
      top = area_map[:n]
      btm = area_map[n:]
      lim = min(len(top), len(btm))

      if compare(top[-lim:], list(reversed(btm[:lim]))) == 1:
         row = n
         break

   return row


def score(mirror):
   total = 0
   m_line = find_mirror_line(mirror)
   d = "X"

   if m_line < 0:
      # swap rows and columns, vertical becomes horizontal
      height = len(mirror)
      width = len(mirror[0])
      transform = [[0 for i in range(height)] for x in range(width)]
      for row in range(height):
         for col in range(width):
            transform[col][row] = mirror[row][col]

      m_line = find_mirror_line(transform)

      if m_line > 0:
         total += m_line
         d = "V"
   else:
      if m_line > 0:
         total += 100 * m_line
         d = "H"

   return (total, m_line, d)


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

mirrors = list()
mirror = list()

for line in lines:
   if line == "":
      mirrors.append(mirror)
      mirror = list()
   else:
      mirror.append(list(line))
mirrors.append(mirror)

total = 0
for mirror in mirrors:
   o_score = score(mirror)
   total += o_score[0]

print(total)
