#!/usr/bin/python

import argparse


# Steps

#     loop from start
#         save min so far
#         if i < min so far, save to temp
#         loop from right of min
#             get the max
#             if max >= max so far, save max

def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - current_min_price_so_far

    for i in range(1, len(prices)-1):
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
        for j in range(i+1, len(prices)):
            temp = prices[j] - current_min_price_so_far
            if  temp > max_profit_so_far:
                max_profit_so_far = temp

    return max_profit_so_far

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
