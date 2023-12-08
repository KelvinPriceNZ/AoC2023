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

times = [ x for x in re.split(r'\s+', lines[0])[1:] ]
dists = [ x for x in re.split(r'\s+', lines[1])[1:] ]

time = int(''.join(times))
dist = int(''.join(dists))

#print(f"{time} {dist}")

wins = 0
victory = 0
for us in range(time+1):
   race = (time - us) * us
   if race > dist:
      wins += 1
      victory = us
      #print(f"{time} {us}us {race} > {dist}")
      break

#print(f"Wins: {wins}")
print(time - victory - victory + 1)
