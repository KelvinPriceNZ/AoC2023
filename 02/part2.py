#!/usr/bin/env python3.12

import os
import sys

import re


def product(l):
   product = 1

   for n in l:
      product *= n

   return product


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

valid_games = list()

for line in lines:
   m = re.match(r'Game (\d+):', line)
   game_num = int(m.group(1))

   game = re.sub(r'^Game \d+:', r'', line)

   rounds = game.split(';')

   max_colours = {
      'red': 0,
      'green': 0,
      'blue': 0
   }

   for hand in rounds:
      samples = hand.split(',')

      for sample in samples:
         m = re.match(r'.*?(\d+)\s+((red|blue|green))', sample)

         count = int(m.group(1))
         colour = m.group(2)

         max_colours[colour] = max(count, max_colours[colour])

   valid_games.append(product(max_colours.values()))

print(sum(valid_games))
