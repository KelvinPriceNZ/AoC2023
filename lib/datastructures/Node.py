class Node:
   x: int
   y: int
   c: int

   def __init__(self, x, y, c):
      self.x = x
      self.y = y
      self.height = c
      self.counter = 0
      self.visited = False

   def __str__(self):
      return f"{self.x}:{self.y} {self.height} {self.visited} C:{self.counter}"

   def __eq__(self, other):
      return self.x == other.x and self.y == other.y

   def next_door(self, n):
      # Orthogonally connected
      connected = False
      if self.x == n.x:
         if self.y == n.y + 1: connected = True
         if self.y == n.y - 1: connected = True
      if self.y == n.y:
         if self.x == n.x + 1: connected = True
         if self.x == n.x - 1: connected = True

      return connected

   def set_counter(self, val):
      self.counter = val

      return self.counter

   def inc_counter(self, inc=1):
      self.counter += inc

      return self.counter
