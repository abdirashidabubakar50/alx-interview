# Prime Game

## Overview
Maria and Ben play a game using a set of consecutive integers starting from 1 up to and including a given number `n`. They take turns picking a prime number from the set and removing that number and its multiples. Maria always goes first. The player who cannot make a move loses the game. The goal of this program is to determine who wins the most rounds after `x` rounds of the game.

## Functionality
The solution is implemented in the `isWinner` function with the following prototype:

```python
def isWinner(x, nums):
```
- **Input**:
  - `x` (int): Number of rounds.
  - `nums` (list of int): Array where each element specifies the `n` value for a round.
- **Output**:
  - Returns the name of the player (`"Maria"` or `"Ben"`) who wins the most rounds.
  - Returns `None` if no player has a majority of wins.

## Example Usage
Given `x = 3` and `nums = [4, 5, 1]`, the game proceeds as follows:

1. **Round 1 (n = 4)**:
   - Maria picks 2, removing 2 and 4.
   - Ben picks 3, removing 3.
   - Ben wins as no prime numbers are left for Maria.

2. **Round 2 (n = 5)**:
   - Maria picks 2, removing 2 and 4.
   - Ben picks 3, removing 3.
   - Maria picks 5, removing 5.
   - Maria wins as no prime numbers are left for Ben.

3. **Round 3 (n = 1)**:
   - Ben wins as no prime numbers are available for Maria to pick.

**Result**: Ben wins more rounds.

```bash
$ ./main.py
Winner: Ben
```

## Key Concepts
- **Prime Number Selection**: Players optimally choose primes to maximize their chances of winning.
- **Efficient Prime Calculation**: Utilizes the Sieve of Eratosthenes for efficient prime number generation.

## Requirements
- Python 3.x
- No additional libraries are required.

## How to Run
1. Clone the repository.
2. Navigate to the folder containing the script.
3. Execute the script using Python:

```bash
python3 main.py
```

## Author
This program was implemented to solve a competitive programming problem involving prime numbers and game theory.

