#!/usr/bin/python3
"""
Minimum Operations

"""


def minOperations(n):
    """Minimum Operations """
    counter = 0
    clipboard = 2
    while n > 1:
        while n % clipboard == 0:
            counter += clipboard
            n /= clipboard
        clipboard += 1
    return counter
