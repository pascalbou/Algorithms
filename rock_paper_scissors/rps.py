#!/usr/bin/python

import sys
import math

# 3 choices to power of n
# create empty list this long

# loop from 0 to len this list
# loop 0 to 2 for rock
# loop 0 to 2 for paper
# loop 0 to 2 for scissors
# append to list each item

def rock_paper_scissors(n):
    result = [[] for i in range(3**n)]
    rps = ['rock', 'paper', 'scissors']

    for a in range(len(result)):     
        result[a].append(rps[math.floor(a/3)])
        result[a].append(rps[a%3])

    # print(result)
    return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')