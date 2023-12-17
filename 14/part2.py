#!/usr/bin/env python3.12

import os
import sys
import re


def roll(table):
   for i, line in enumerate(table):
      ln = ''.join(line)
      s = re.sub(r'(\.+)(O)', r'\2\1', ln)
      while s != ln:
         ln = s
         s = re.sub(r'(\.+)(O)', r'\2\1', ln)
      table[i] = list(s)
   return table


def north(table):
   height = len(table)
   width = len(table[0])

   xform = [[ table[x][y] for x in range(height)] for y in range(width)]

   xform = roll(xform)

   return [[ xform[x][y] for x in range(height)] for y in range(width)]


def south(table):
   height = len(table)
   width = len(table[0])

   xform = [[ table[x][y] for x in range(height)] for y in range(width)]

   xform = east(xform)

   return [[ xform[x][y] for x in range(height)] for y in range(width)]


def east(table):
   xform = [ list(reversed(line)) for line in table ]
   west(xform)
   return [ list(reversed(line)) for line in xform ]


def west(table):
   return roll(table)


def show(table):
   for row in table:
      print(''.join(row))
   print()
   #input()


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

height = len(lines)
width = len(lines[0])

xform = lines
#show(xform)
cache = dict()
for x in range(1,31):
   for i in range(x):
      xform = north(xform)
      #show(xform)
      xform = west(xform)
      #show(xform)
      xform = south(xform)
      #show(xform)
      xform = east(xform)
      #show(xform)
   #show(xform)

   total = 0
   for i, line in enumerate(xform):
      oes = sum([1 for x in line if x == 'O'])
      score = (height - i) * oes
      total += score

   if total not in cache:
      cache[total] = list()

   cache[total].append(x)
   print(f"{x:7} {total:5}")

"""
After the above, a cycle should be visible
So, next ...
Remove anything that only occurs once (will be from before cycle starts)

See how long your cycle is, in my case, 9
"""

for k in cache.copy().keys():
   print(f"{k:4}|{cache[k]}")
   if len(cache[k]) == 1:
      del cache[k]

print()
for k in sorted(cache.keys()):
   print(f"{k:4}|{cache[k]}")

cycle_length = 9
print()
for k in sorted(cache.keys()):
   print(f"{k:4}|{set([ x % cycle_length for x in cache[k] ])}")

g = 1_000_000_000 % cycle_length
print(f"Look for {g} in the table above, the key is your answer")

"""
So now, whatever 1,000,000,000 mod cycle_length is will appear in the table
"""

print()
for x in cache:
   if g + 18 in cache[x]:
      print(x)
