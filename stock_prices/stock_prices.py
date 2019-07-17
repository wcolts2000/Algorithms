#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # place to track the current min price
    current_min_price = int(prices[0])
    # place to track the current max profit
    current_max_profit = int(prices[1]) - current_min_price

    for i in range(len(prices) - 1):
        # if current_min_price == None:
        #     current_min_price = i
        # if current_max_profit == None:
        #     current_max_profit = prices[1] - current_min_price
        if int(prices[i]) < current_min_price:
            current_min_price = int(prices[i])
        if int(prices[i + 1]) - current_min_price > current_max_profit:
            current_max_profit = int(prices[i + 1]) - current_min_price

    return current_max_profit


# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))

# return the max_profit from a single buy/sell (must buy first)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
