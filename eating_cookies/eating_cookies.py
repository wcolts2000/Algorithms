#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    eat3 = 2
    eat2 = 1
    eat1 = 1

    for i in range(n-2):
        r = eat3 + eat2 + eat1
        eat1 = eat2
        eat2 = eat3
        eat3 = r

    return r


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
