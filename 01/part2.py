#!/usr/bin/env python3.12

import os
import sys

import re


def numify(m):
   w = m.group(1)
   w = re.sub(r'(zero|orez)', r'0', w)
   w = re.sub(r'(one|eno)', r'1', w)
   w = re.sub(r'(two|owt)', r'2', w)
   w = re.sub(r'(three|eerht)', r'3', w)
   w = re.sub(r'(four|ruof)', r'4', w)
   w = re.sub(r'(five|evif)', r'5', w)
   w = re.sub(r'(six|xis)', r'6', w)
   w = re.sub(r'(seven|neves)', r'7', w)
   w = re.sub(r'(eight|thgie)', r'8', w)
   w = re.sub(r'(nine|enin)', r'9', w)
   return w


BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

numbers = list()

for line in lines:
   line = re.sub(r'^(zero|one|two|three|four|five|six|seven|eight|nine)', numify, line)
   line = re.sub(r'(zero|one|two|three|four|five|six|seven|eight|nine)$', numify, line)
   line = re.sub(r'^\D*?(zero|one|two|three|four|five|six|seven|eight|nine)', numify, line, count=1)
   line = re.sub(r'^\D*?(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', numify, line[::-1], count=1)
   line = line[::-1]
   line = re.sub(r'\D+', r'', line)
   digit1 = 10 * int(re.sub(r'^(\d{1}).*$', r'\1', line))
   digit2 = int(re.sub(r'^.*(\d{1})$', r'\1', line))
   number = digit1 + digit2
   numbers.append(number)

print(sum(numbers))
