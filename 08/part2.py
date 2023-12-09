#!/usr/bin/env python3.12

import os
import sys
import re
import math
from dataclasses import dataclass


@dataclass
class Node:
    name: str
    left: str
    right: str

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.name} = ({self.left}, {self.right})"


def left_or_right(dirs):
    l = len(dirs)
    i = 0
    while True:
        yield dirs[i]
        i = (i + 1) % l


def ends_with_Z(l):
    for i in l:
        if not i.name[2] == "Z": return False
    return True


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt.big")

lines = list()

with open(INPUT, "r") as f:
    lines.extend(f.read().splitlines())

desert_map = lines[0]

nodes = dict()

for line in lines[2:]:
    m = re.match(r'([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)', line)

    name = m.group(1)
    left = m.group(2)
    right = m.group(3)

    n = Node(name, left, right)

    nodes[name] = n

current_nodes = [nodes[n] for n in nodes.keys() if n.endswith('A')]

nums = list()

for node in current_nodes:
    journey = 0
    directions = left_or_right(desert_map)
    current_node = node
    #print(f"{current_node} {journey}")
    while not current_node.name[2] == 'Z':
        d = next(directions)
        journey += 1
        if d == "L":
            current_node = nodes[current_node.left]
        else:
            current_node = nodes[current_node.right]
    nums.append(journey)
    #print(f"{current_node} {journey}")

# Find LCM of the numbers
# The sequence for each ??A goes in a cycle so the LCM of each journey will get them all lined up

print(math.lcm(*nums))
