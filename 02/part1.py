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

max_colours = {
   'red': 12,
   'green': 13,
   'blue': 14
}

valid_games = list()

for line in lines:
   m = re.match(r'Game (\d+):', line)
   game_num = int(m.group(1))

   game = re.sub(r'^Game \d+:', r'', line)

   rounds = game.split(';')

   valid = True

   for hand in rounds:
      samples = hand.split(',')

      for sample in samples:
         m = re.match(r'.*?(\d+)\s+((red|blue|green))', sample)

         count = int(m.group(1))
         colour = m.group(2)

         if count > max_colours[colour]:
            valid = False

   if valid:
      valid_games.append(game_num)

print(sum(valid_games))
