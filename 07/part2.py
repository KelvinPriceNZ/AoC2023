#!/usr/bin/env python3.12

import os
import sys
from dataclasses import dataclass
from functools import total_ordering
from functools import cmp_to_key


card_value = {
   '2': 1,
   '3': 2,
   '4': 3,
   '5': 4,
   '6': 5,
   '7': 6,
   '8': 7,
   '9': 8,
   'T': 9,
   'J': 0,
   'Q': 11,
   'K': 12,
   'A': 13,
}

hand_type = {
   7: "5 of a kind",
   6: "4 of a kind",
   5: "Full house",
   4: "3 of a kind",
   3: "2 pair",
   2: "1 pair",
   1: "High card",
}


@dataclass
@total_ordering
class Hand:
   cards: str
   rank: int
   bid: int
   type_of_hand: str

   def __init__(self, hand, bid):
      self.cards = hand
      self.bid = bid
      self.rank = self.rank_hand(hand)
      self.type_of_hand = hand_type[self.rank]


   def rank_hand(self, cards):
      pile = { x : 0 for x in list('23456789TJQKA') }
      for card in cards:
         pile[card] += 1

      high = max(pile.values())
      jokers = pile['J']
      pairs = len([ x for x in pile.values() if x == 2 ])

      if high == 5: return 7 # 5 of a kind

      if high == 4:
         if jokers == 4: return 7
         if jokers == 1: return 7
         return 6 # 4 of a kind

      if high == 3:
         if jokers == 2: return 7
         if jokers == 3:
            if pairs == 1: return 7
            return 6
         if jokers == 1: return 6
         if pairs == 1: return 5 # Full house
         return 4 # 3 of a kind

      if high == 2:
         if jokers == 2 and pairs == 2: return 6
         if jokers == 1 and pairs == 2: return 5
         if jokers == 2 and pairs == 1: return 4
         if jokers == 1 and pairs == 1: return 4
         if jokers == 0 and pairs == 2: return 3 # 2 pair
         return 2 # 1 pair

      if high == 1:
         if jokers == 1: return 2
         return 1 # High card

   def __eq__(self, other):
      return self.cards == other.cards

   def __lt__(self, other):
      if self.rank < other.rank: return True

      for i in range(5):
         if card_value[self.cards[i]] < card_value[other.cards[i]]: return True

      return False

   def __gt__(self, other):
      if self.rank > other.rank: return True

      for i in range(5):
         if card_value[self.cards[i]] > card_value[other.cards[i]]: return True

      return False

def hand_splat(h: Hand):
   s = str(h.rank)
   for c in h.cards:
      s += f"{card_value[c]:2d}"
   return s

BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DAY = os.path.basename(BASEDIR)

INPUT = os.path.abspath(f"{BASEDIR}/../input/{DAY}/input.txt")

lines = list()

with open(INPUT, "r") as f:
   lines=f.read().splitlines()

hands = list()

for line in lines:
   ( hand, bid ) = line.split(' ')
   dealt = Hand(hand, bid)
   hands.append(dealt)

hands.sort(key=hand_splat)

total = 0
for s, a_hand in enumerate(hands):
   total += (s + 1) * int(a_hand.bid)
   #print(f"{s:5d} {a_hand}")

print(total)
