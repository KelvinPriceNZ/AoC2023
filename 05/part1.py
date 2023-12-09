#!/usr/bin/env python3.12

import os
import sys
import re
import math


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

seeds = [ int(x) for x in re.split(r'\s+', lines[0])[1:] ]

link = ''
seed_map = dict()

for line in lines[2:]:
   m = re.match(r'(\S+)\s+map:', line)

   if m:
      link = m.group(1)
      seed_map[link] = list()
   else:
      nums = [ int(x) for x in re.split(r'\s+', line) if len(line) > 0 ]
      if len(nums) == 3:
         dst_start = nums[0]
         src_start = nums[1]
         range_len = nums[2]

         seed_map[link].append((dst_start, src_start, range_len))

links = seed_map.keys()
lowest = math.inf

for seed in seeds:
   goal = seed
   for link in links:
      found = False
      map_range = None
      for t in seed_map[link]:
         (d, s, r) = t
         if goal >= s and goal <= s + r - 1:
            found = True
            map_range = t
            break

      if found:
         d, s, r = map_range
         goal = (goal - s) + d

   if goal < lowest:
      lowest = goal
   #print(f"{seed} {link} {goal}")

print(lowest)
