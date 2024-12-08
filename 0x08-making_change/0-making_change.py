#!/usr/bin/python3

"""This module defines a function that determine
the fewest number of  coins needed to meet a givent amount (total)
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount(total)

    Args:
        coins: a list of the value of coins in possession
        total:The total amount to be met with the fewest number of coins.

    Returns:
        fewest number of coins needed to meet total
        if total is 0 return 0
        else if total cannot be met by any number of coins you have return -1
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total > 0:
        return -1

    return count
