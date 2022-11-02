"""
The interns at Amazon were asked to review the company’s stock value over a period. Given the stock prices of n months,
 the net price change for the ith month is defined as the absolute difference between the average of stock prices for
 the first i months and for the remaining (n – i) months where 1≤ i
Given an array of stock prices, find the month at which the net price change is minimum. If there are several such
months, return the earliest month.

Note: The average of a set of integers here is defined as the sum of integers divided by the number of integers,
rounded down to the nearest integer. For example, the average of [1, 2, 3, 4] is the floor of (1 + 2 + 3 + 4) / 4 = 2.5
and the floor of 2.5 is 2.

Example
stockPrice = [1, 3, 2, 3]

The minimum net price change is 0, and it occurs in the 2nd month. Return 2.

Function Description
Complete the function findEarliestMonth the editor below.

findEarliestMonth has the following parameter: int stockPrice[n]: the stock prices

Returns
int: the earliest month in which the net price change is minimum

Constraints
2 ≤ n ≤ 105

1 ≤ stockPrice[i] ≤ 109

Sample Input
STDIN FUNCTION

------ ----------

5 -> stockPrice[]

size n = 5

1 -> stockPrice = [1, 3, 2, 4, 5]

3 2 4 5

Sample Output
2

Explanation
The net price change can be calculated as:

Month 1: [1] and [3, 2, 4, 5], their respective averages, rounded down = 1 and 3, net price change = 2

Month 2: [1, 3] and [2, 4, 5], averages = 2 and 3, net price change = 1

Month 3: [1, 3, 2] and [4, 5], averages = 2 and 4, net price change = 2

Month 4: [1, 3, 2, 4] and [5], averages = 2 and 5, net price change = 3

The minimum net price change is 1, and it occurs at month 2.

Sample Input 1
STDIN FUNCTION

------ ----------

6 -> stockPrice[]

size n = 6

1 -> stockPrice = [1, 1, 1, 1, 1, 1]

1 1 1 1 1

Sample Output 1
1

Explanation
Since all the stock prices are all the same, the average is always 1 and the net price change is always 0.
The earliest month this occurs is 1.


"""

# SOLUTION
# initialize month variable with 0

# importing reduce()
from functools import reduce

import running_time


# average of list
def average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


# difference between average
def diff(t):
    return [abs(j - i) for i, j in zip(t[:-1], t[1:])]


def findEarliestMonth(stockPrice):
    n = len(stockPrice)
    d = {}
    # g = {}
    # x = {}
    # y = {}

    for i in range(1, n):
        # x[i] = [stockPrice[:i], stockPrice[i:n + 1]]
        # y[i] = [average(stockPrice[:i]), average(stockPrice[i:n + 1])]
        # g[i] = [int(average(stockPrice[:i])), int(average(stockPrice[i:n + 1]))]
        d[i] = diff([int(average(stockPrice[:i])), int(average(stockPrice[i:n + 1]))])
    # print(x)
    # print(y)
    # print(g)
    # print(d)
    month = min(d, key=d.get)
    return month


if __name__ == "__main__":
    # arr1 = [1, 1, 1, 1, 1, 1]
    # arr2 = [1, 3, 2, 4, 5]
    arr3 = [
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3,
        2, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1, 5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1,
        3, 2, 4, 5, 1, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1,
        3, 2, 4,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3,
        2, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1, 5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4,
        5, 1, 3, 2, 4, 5, 1,
        3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 51, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2,
        4, 5, 1, 3, 2, 4, 5, 1]
    print(findEarliestMonth(arr3))
    running_time.time_to_run()
