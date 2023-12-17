#!/usr/bin/env python3.10

import os
import sys
import numpy as np


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
   found = False
   row = -1
   for n in range(len(mirror)):
      row += 1
      if n == 0: continue
      size = len(mirror)
      top = mirror[:n]
      btm = mirror[n:]
      lim = min(len(top), len(btm))

      if top[-lim:] == list(reversed(btm[:lim])):
         found = True
         total += 100 * row
         break

   if not found:
      # swap rows and columns, vertical becomes horizontal
      #transform = np.array(mirror).T.tolist()
      height = len(mirror)
      width = len(mirror[0])
      transform = [[0 for i in range(height)] for x in range(width)]
      for row in range(height):
         for col in range(width):
            transform[col][row] = mirror[row][col]

      row = -1
      for n in range(len(transform)):
         row += 1
         if n == 0: continue
         size = len(transform)
         top = transform[:n]
         btm = transform[n:]
         lim = min(len(top), len(btm))

         if top[-lim:] == list(reversed(btm[:lim])):
            found = True
            total += row
            break

print(total)
