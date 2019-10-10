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


    # n=3

    result[0].append(rps[0])
    result[1].append(rps[0])
    result[2].append(rps[0])
    result[3].append(rps[0])
    result[4].append(rps[0])
    result[5].append(rps[0])
    result[6].append(rps[0])
    result[7].append(rps[0])
    result[8].append(rps[0])
    result[9].append(rps[0])
    result[10].append(rps[1])
    result[11].append(rps[1])
    result[12].append(rps[1])
    result[13].append(rps[1])
    result[14].append(rps[1])
    result[15].append(rps[1])
    result[16].append(rps[1])
    result[17].append(rps[1])
    result[18].append(rps[2])
    result[19].append(rps[2])
    result[20].append(rps[2])
    result[21].append(rps[2])
    result[22].append(rps[2])
    result[23].append(rps[2])
    result[24].append(rps[2])
    result[25].append(rps[2])
    result[26].append(rps[2])

    result[0].append(rps[0])
    result[1].append(rps[0])
    result[2].append(rps[0])
    result[3].append(rps[0])
    result[4].append(rps[0])
    result[5].append(rps[0])
    result[6].append(rps[0])
    result[7].append(rps[0])
    result[8].append(rps[0])
    result[9].append(rps[0])
    result[10].append(rps[1])
    result[11].append(rps[1])
    result[12].append(rps[1])
    result[13].append(rps[1])
    result[14].append(rps[1])
    result[15].append(rps[1])
    result[16].append(rps[1])
    result[17].append(rps[1])
    result[18].append(rps[2])
    result[19].append(rps[2])
    result[20].append(rps[2])
    result[21].append(rps[2])
    result[22].append(rps[2])
    result[23].append(rps[2])
    result[24].append(rps[2])
    result[25].append(rps[2])
    result[26].append(rps[2])

    result[0].append(rps[0])
    result[1].append(rps[0])
    result[2].append(rps[0])
    result[3].append(rps[1])
    result[4].append(rps[1])
    result[5].append(rps[1])
    result[6].append(rps[2])
    result[7].append(rps[2])
    result[8].append(rps[2])
    result[9].append(rps[0])
    result[10].append(rps[0])
    result[11].append(rps[0])
    result[12].append(rps[1])
    result[13].append(rps[1])
    result[14].append(rps[1])
    result[15].append(rps[2])
    result[16].append(rps[2])
    result[17].append(rps[2])
    result[18].append(rps[0])
    result[19].append(rps[0])
    result[20].append(rps[0])
    result[21].append(rps[1])
    result[22].append(rps[1])
    result[23].append(rps[1])
    result[24].append(rps[2])
    result[25].append(rps[2])
    result[26].append(rps[2])

    result[0].append(rps[0])
    result[1].append(rps[1])
    result[2].append(rps[2])
    result[3].append(rps[0])
    result[4].append(rps[1])
    result[5].append(rps[2])
    result[6].append(rps[0])
    result[7].append(rps[1])
    result[8].append(rps[2])
    result[9].append(rps[0])
    result[10].append(rps[1])
    result[11].append(rps[2])
    result[12].append(rps[0])
    result[13].append(rps[1])
    result[14].append(rps[2])
    result[15].append(rps[0])
    result[16].append(rps[1])
    result[17].append(rps[2])
    result[18].append(rps[0])
    result[19].append(rps[1])
    result[20].append(rps[2])
    result[21].append(rps[0])
    result[22].append(rps[1])
    result[23].append(rps[2])
    result[24].append(rps[0])
    result[25].append(rps[1])
    result[26].append(rps[2])


    # n=2
    result[0].append(rps[0])
    result[1].append(rps[0])
    result[2].append(rps[0])
    result[3].append(rps[1])
    result[4].append(rps[1])
    result[5].append(rps[1])
    result[6].append(rps[2])
    result[7].append(rps[2])
    result[8].append(rps[2])

    result[0].append(rps[0])
    result[1].append(rps[1])
    result[2].append(rps[2])
    result[3].append(rps[0])
    result[4].append(rps[1])
    result[5].append(rps[2])
    result[6].append(rps[0])
    result[7].append(rps[1])
    result[8].append(rps[2])


    # n=1
    result[0].append(rps[0])
    result[1].append(rps[1])
    result[2].append(rps[2])

    # print(result)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
