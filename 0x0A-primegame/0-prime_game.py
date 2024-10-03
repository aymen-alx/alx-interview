#!/usr/bin/python3
"""
Prime game winner determination
"""


def isWinner(num_rounds, round_limits):
    """
    Determines the winner of the Prime Game.

    Args:
        num_rounds (int): Number of rounds of the game.
        round_limits (list[int]): Upper limits of ranges for each round.

    Returns:
        The name of the winner (Maria or Ben), or
        None if there is no clear winner.
    """

    if not num_rounds or not round_limits:
        return None

    maria_wins = ben_wins = 0

    for round_limit in round_limits:
        primes_in_round = generate_primes_optimized(round_limit)
        if len(primes_in_round) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def generate_primes_optimized(upper_bound):
    """
    Generates a list of prime numbers between 1 and the upper bound,
    inclusive, using an optimized Sieve of Eratosthenes algorithm.

    Args:
        upper_bound (int): The upper bound of the range.

    Returns:
        A list of prime numbers within the specified range.
    """

    if upper_bound < 2:
        return []

    primes = [2]
    sieve = [True] * (upper_bound + 1)

    for p in range(3, upper_bound + 1, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, upper_bound + 1, p * 2):
                sieve[i] = False

    return primes
