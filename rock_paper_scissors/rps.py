#!/usr/bin/python

import sys

# 3 choices to power of n
# create empty list this long

# loop from 0 to len this list
# loop 0 to 2 for rock
# loop 0 to 2 for paper
# loop 0 to 2 for scissors
# append to list each item

def rock_paper_scissors(n):
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')