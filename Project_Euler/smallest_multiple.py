"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""
import math

import running_time


def compute(n):
    value = 2
    for i in range(2, n + 1):
        value *= i // gcd(i, value)
    return value


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


if __name__ == '__main__':
    print(compute(10))
    running_time.time_to_run()
