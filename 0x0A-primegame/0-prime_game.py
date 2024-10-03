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
    if num_rounds < 1 or not round_limits:
        return None

    maria_wins = 0
    ben_wins = 0

    n = max(round_limits)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for num_rounds in range(2, int(n**0.5) + 1):
        if primes[num_rounds]:
            for y in range(num_rounds**2, n + 1, num_rounds):
                primes[y] = False

    for n in round_limits:
        count = sum(primes[2:n+1])
        ben_wins += count % 2 == 0
        maria_wins += count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
