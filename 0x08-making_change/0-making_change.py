#!/usr/bin/python3
"""
Greedy Algorithm to find Minimum number of Coins
"""


def makeChange(coins, total):
    """
    Greedy Algorithm
    """
    if total <= 0:
        return 0
    result = []
    coins.sort(reverse=True)
    length = len(coins)

    for coin in coins:
        while total >= coin:
            total -= coin
            result.append(coin)

    if total > 0 or len(result) == 0:
        return -1
    else:
        return len(result)
