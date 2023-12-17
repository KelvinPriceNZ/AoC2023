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

xform = [[ lines[x][y] for x in range(height)] for y in range(width)]

for i, line in enumerate(xform):
   ln = ''.join(line)
   s = re.sub(r'(\.+)(O)', r'\2\1', ln)
   while s != ln:
      ln = s
      s = re.sub(r'(\.+)(O)', r'\2\1', ln)
   xform[i] = list(s)

xform = [[ xform[x][y] for x in range(height)] for y in range(width)]
total = 0
for i, line in enumerate(xform):
   oes = re.sub(r'[^O]+', r'', ''.join(line))
   score = (height - i) * len(oes)
   total += score

print(total)
