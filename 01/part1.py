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

numbers = list()

for line in lines:
   line = re.sub(r'\D+', r'', line)
   digit1 = 10 * int(re.sub(r'^(\d).*$', r'\1', line))
   digit2 = int(re.sub(r'^.*(\d)$', r'\1', line))
   number = digit1 + digit2
   numbers.append(number)

print(sum(numbers))
