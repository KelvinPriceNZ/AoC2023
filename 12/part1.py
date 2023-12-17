#!/usr/bin/env python3.12

import os
import sys
import re
import random
from itertools import permutations, combinations


def dfs(l, lim, n, c, depth):
   if depth == 1:
      r = lim - sum(l)
      l.append(r)
      yield l
      l.pop()
      return

   for x in range(n + 1):
      l.append(x)
      yield from dfs(l, lim, n - x, c, depth - 1)
      l.pop()


def gen(rule, pattern):
   hashes = sum(rule) + len(rule) - 1
   length = len(pattern)
   limit = length - hashes
   seeds = [ '#' * n + '.' for n in rule ]
   seeds[-1] = '#' * rule[-1]
   seeds.append("")
   cols = len(seeds)
   dots = dfs([], limit, limit, cols, cols)
   # Put poss patterns in to s (list or set)
   s = set()
   for d in dots:
      p = ''
      for n in range(cols):
         p += '.' * d[n]
         p += seeds[n]
      s.add(p)

   results = list()
   for p in s:
      matched = True
      for pair in zip(pattern, p):
         left, right = pair
         if left != '?' and left != right:
            matched = False
            break
      if matched:
         results.append(p)

   return results


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

total = 0
for line_num, line in enumerate(lines):
   ( pattern, rule ) = line.split(' ')
   rule = [ int(x) for x in rule.split(',') ]
   choices = gen(rule, pattern)
   for choice in choices:
      print(f"{pattern} | {choice} | {rule}")
   total += len(choices)
   print(f"{line_num:5} | {total:7} (+{len(choices)})")
print(f"Final total is {total}")
