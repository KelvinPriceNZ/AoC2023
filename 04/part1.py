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

points = list()

for line in lines:
   card = re.sub(r'Card\s+\d+:\s+', r'', line)
   card = re.sub(r'\s+', ' ', card)
   game, ticket = card.split('|')
   game_numbers = set([int(x) for x in game.split(' ') if x])
   ticket_numbers = set([int(x) for x in ticket.split(' ') if x])

   common = game_numbers.intersection(ticket_numbers)

   exp = len(common) - 1

   if exp >= 0:
      points.append(2 ** exp)

print(sum(points))
