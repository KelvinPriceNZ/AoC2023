#!/usr/bin/env python3.12

import os
import sys
import re
from collections import deque

BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

points = dict()

for line in lines:
   m = re.match(r'Card\s+(\d+):\s+', line)
   card_num = int(m.group(1))
   card = re.sub(r'Card\s+\d+:\s+', r'', line)
   card = re.sub(r'\s+', ',', card)
   game, ticket = card.split('|')
   game_numbers = set([x for x in game.split(',') if x])
   ticket_numbers = set([x for x in ticket.split(',') if x])

   common = game_numbers & ticket_numbers

   score = len(common)

   bonus = [x for x in range(card_num + 1, card_num + score + 1)]

   #print(f"{card_num}: {score} {bonus}")

   bonus.insert(0, card_num)
   points[card_num] = bonus

queue = deque(sorted(points.keys()))

total = 0
while len(queue) > 0:
   total += 1
   n = queue.popleft()
   if len(points[n]) <= 1: continue
   queue.extend(points[n][1:])

print(total)