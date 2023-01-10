"""
Your quirky boss collects rare, old coins...

They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.
"""


def change_possibilities_top_down(amount, denominations):
    n = len(denominations)

    # ways is an array, where from 0 cents to the target amount
    # ways holds a list of ways the given denominations can sum to the target
    # amount
    ways = [[0 for x in range(n)] for z in range(amount + 1)]

    # Using a dynamic solution, determine the ways for every postive
    # amount less than our target amount, building a table, a cache of
    # amounts that help us find the number of ways for the target
    # amount

    # for each amount from 0 up to our target amount
    for curr_amt in range(1, amount + 1):

        # find the number of ways of using all the coins to sum to the
        # current amount by looping over each coin
        for coin in range(n):

            # 1. find ways to get to the current amount minus our current coin
            sub_amount = curr_amt - denominations[coin]
            if sub_amount < 0:
                sub_amt_ways = 0
            elif sub_amount == 0:
                sub_amt_ways = 1
            else:
                sub_amt_ways = ways[sub_amount][coin]

            # 2. lookup the prior ways we found to get the current
            #    amount with the prior coins
            # here's where the dynamics occurs:
            old_ways = ways[sub_amount][coin - 1]

            # the total ways is the sum of both ways
            ways[curr_amt][coin] = sub_amt_ways + old_ways

    count = ways[amount][n - 1]

    return count


print(change_possibilities_top_down(4, [1, 2, 3]))
