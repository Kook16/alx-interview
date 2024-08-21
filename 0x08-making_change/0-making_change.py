#!/usr/bin/python3
'''makeChanges function'''


def makeChange(coins, total):
    '''
    fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Initialize dp array with inf and set dp[0] to 0
    dp = [0] + [float('inf')] * total

    # Sort coins in descending order to consider larger coins first
    coins.sort(reverse=True)

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
