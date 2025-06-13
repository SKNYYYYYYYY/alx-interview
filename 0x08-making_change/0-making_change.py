#!/usr/bin/python3
"""Dynamic programming"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amt in range(coin, total + 1):
            dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
