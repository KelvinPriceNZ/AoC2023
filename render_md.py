#!/usr/bin/env python3.11

import os
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

puzzle_day = int(sys.argv[1])

j2env = Environment( loader=FileSystemLoader(".") )
j2template = j2env.get_template("./Puzzle.md.j2")

md = j2template.render(day=puzzle_day)

with open(f"{puzzle_day:02d}/Puzzle.md", "w") as f:
   f.write(md)
