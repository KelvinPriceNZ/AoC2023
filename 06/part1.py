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

times = [ int(x) for x in re.split(r'\s+', lines[0])[1:] ]
dists = [ int(x) for x in re.split(r'\s+', lines[1])[1:] ]

product = 1
for pair in zip(times, dists):
   (time, dist) = pair
   wins = 0
   for us in range(time+1):
      race = (time - us) * us
      if race > dist:
         wins += 1
         #print(f"{time} {us} {race} > {dist}")

   product *= wins
   #print(f"Wins: {wins}")

print(product)
