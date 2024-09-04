#!/usr/bin/python3
''' Prime Game Challenge - Determines the winner after x rounds. '''


def isWinner(x, nums):
    """Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list of int): List of n for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"),
             or None if there is no clear winner.
    """
    if not nums or x < 1:
        return None

    # Calculate the maximum number in nums to sieve primes up to that number
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Prepare prefix sum to count primes up to any number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Initialize win counts for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play x rounds
    for n in nums:
        if prime_count[n] % 2 == 1:
            # Maria wins if the count of primes is odd
            maria_wins += 1
        else:
            # Ben wins if the count of primes is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
