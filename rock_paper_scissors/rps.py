#!/usr/bin/python

import sys
import math


def rock_paper_scissors(n):
    result = []
    rps = ['rock', 'paper', 'scissors']

    def inner_rps(m, lst):
        if m == 0:
            result.append(lst)
            return

        for i in rps:
            lst += [i]
            inner_rps(m-1, lst)

    inner_rps(n, result)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
