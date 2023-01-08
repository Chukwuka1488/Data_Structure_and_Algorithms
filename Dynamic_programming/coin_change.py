"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
import math


def coinChange(coins, amount):
    # table[i] will be storing the number of solutions for
    # value i. We need sum+1 rows as the table is constructed
    # in bottom up manner using the base case (sum = 0)
    # Initialize all table values as 0
    n = len(coins)
    cache = [[math.inf] * (amount + 1) for _ in range(n)]
    # cache[0] = 1

    for i in range(n):
        cache[i][0] = 0
        for j in range(1, amount + 1):
            if i >= 0:
                cache[i][j] = cache[i - 1][j]  # Skip i_th coin
            if j >= coins[i]:
                cache[i][j] = min(cache[i][j], cache[i][j - coins[i]] + 1)  # Use i_th coin

    return cache[n - 1][amount] if cache[n - 1][amount] != math.inf else -1


print(coinChange([1, 2, 5], 11))
