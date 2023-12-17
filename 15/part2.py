#!/usr/bin/env python3.12

import os
import re
import sys
from collections import deque
from dataclasses import dataclass


@dataclass
class Lens:
   label: int
   focal_length: int

   def __init__(self, label, flen):
      self.label = label
      self.focal_length = flen

   def __str__(self):
      return f"[{self.label} {self.focal_length}]"

   def __eq__(self, other):
      return self.label == other.label


def hash_map(code):
   hm = 0
   for c in code:
      hm += ord(c)
      hm *= 17
      hm %= 256
   return hm


opcode = {
   "=": "PUSH",
   "-": "POP",
}

BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

boxes = { x : deque() for x in range(256) }

for line in lines:
   for code in line.split(","):
      m = re.match(r'([^=-]+)([=-])(.*)$', code)
      lbl = m.group(1)
      op = m.group(2)
      flen = m.group(3)
      box_num = hash_map(lbl)
      #print(f"{opcode[op]:4}|{box_num:3}|{lbl:4}|{flen}")
      if op == '=':
         lens = Lens(lbl, int(flen))
         if lens in boxes[box_num]:
            pos = boxes[box_num].index(lens)
            boxes[box_num][pos] = lens
         else:
            boxes[box_num].append(lens)
      if op == '-':
         if len(boxes[box_num]):
            old_lens = None
            for lens in boxes[box_num]:
               if lbl == lens.label:
                  old_lens = lens
            if old_lens:
               boxes[box_num].remove(old_lens)
      """
      for box in boxes:
         if len(boxes[box]):
            for slot, lens in enumerate(boxes[box]):
               print(f"{box}:{slot + 1}:{lens}")
      """

total = 0
for box in boxes:
   if len(boxes[box]):
      for slot, lens in enumerate(boxes[box]):
         val = (box + 1) * (slot + 1) * lens.focal_length
         #print(f"{box + 1} * {slot + 1} * {lens.focal_length} = {val}")
         total += val

print(total)
