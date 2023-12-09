#!/usr/bin/env python3.12

import os
import sys
import re
from dataclasses import dataclass

@dataclass
class Node:
   name: str
   left: str
   right: str

   def __init__(self, n, l, r):
      self.name = n
      self.left = l
      self.right = r


def left_or_right(desert_map):
   l = len(desert_map)
   i = 0
   while True:
      yield desert_map[i]
      i = (i + 1) % l


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

desert_map = lines[0]

nodes = dict()

for line in lines[2:]:
   m = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)

   name = m.group(1)
   left = m.group(2)
   right = m.group(3)

   n = Node(name, left, right)

   nodes[name] = n

current_node = 'AAA'
journey = 0
directions = left_or_right(desert_map)

while current_node != 'ZZZ':
   d = next(directions)
   journey += 1
   if d == "L":
      current_node = nodes[current_node].left
   else:
      current_node = nodes[current_node].right

   #print(f"{current_node} {journey}")

print(journey)
