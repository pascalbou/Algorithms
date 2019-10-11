#!/usr/bin/python

import sys


def making_change(amount, denominations):
    ways = [0 for _ in range(amount+1)]
    ways[0] = 1

    for i in range(len(denominations)):
        for j in range(len(ways)):
            if (denominations[i] <= j):
                ways[j] += ways[j-denominations[i]]

    return ways[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
