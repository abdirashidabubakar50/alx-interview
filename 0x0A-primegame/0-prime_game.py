#!/usr/bin/python3
"""
This file implements the solution for a game played between
Maria and Ben involving prime numbers.

Overview:
Maria and Ben play a game involving a set of consecutive integers
from 1 to n for x rounds. They take turns choosing a prime number
and removing that number along with its multiples. The player unable
to make a move loses.Maria always goes first, and both players play optimally.
The goal is to determine the winner of each round
and return the player with the most wins across all rounds.

Functions:
1. sieve_of_eratosthenes(max_n):
   Computes a boolean list of prime numbers up to a given maximum
   using the Sieve of Eratosthenes algorithm.

2. count_primes_up_to(primes, n):
   Counts the number of prime numbers up to a given value `n` using a
   precomputed primes list.

3. isWinner(x, nums):
   Determines the winner of the game after `x` rounds and returns the
   name of the player with the most wins.

Implementation Details:
- The Sieve of Eratosthenes is used for efficient prime computation.
- Optimal gameplay is assumed for both Maria and Ben.
- The result is determined by counting the number of primes
up to each `n` for every round.

Usage:
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))

Returns:
- "Maria" if Maria wins the most rounds.
- "Ben" if Ben wins the most rounds.
- None if the result is a tie.
"""


def sieve_of_eratosthenes(max_n):
    """
    Computes a boolean list where True indicates that the index
    is a prime number.

    Args:
        max_n (int): The maximum number to compute primes up to.

    Returns:
        list: A boolean list with True at prime indices.
    """
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    return primes


def count_primes_up_to(primes, n):
    """
    Counts the number of primes up to a given number `n`.

    Args:
        primes (list): A boolean list indicating prime numbers.
        n (int): The upper limit to count primes up to.

    Returns:
        int: The count of prime numbers up to `n`.
    """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """
    Determines the winner of the prime number game after `x` rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the maximum number
        in each round.

    Returns:
        str or None: The name of the player with the most wins
        ("Maria" or "Ben"), or None if tied.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(primes, n)
        # Maria wins if the number of primes is odd; otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
