"""
Given some positive integer n, write a method to return the fewest number of perfect square numbers which sum to n.
n = 28
howManySquares(n);
// 4
// 16 + 4 + 4 + 4 = 28, so 4 numbers are required
// 25 + 1 + 1 + 1 = 28

Solution
1. set the range of n to -1
"""
import math
from functools import lru_cache


@lru_cache(None)
def dp(n):
    # a = []
    if n == 0:
        return 0
    else:
        min_val = float("inf")
        b = math.floor(math.sqrt(n))
        for x in range(b):
            min_val = min(min_val, dp(n - (x + 1) ** 2))
            # a.append(min_val + 1)
        return min_val + 1


def numSquares(n):
    return dp(n)


if __name__ == "__main__":
    print(numSquares(12))
#
# import unittest
#
#
# class Test(unittest.TestCase):
#     def test_1(self):
#         assert howManySquares(16) == 1
#         print("PASSED: howManySquares(16) should return 1")
#
#     def test_2(self):
#         assert howManySquares(6) == 3
#         print("PASSED: howManySquares(1) should return 1")
#
#     def test_3(self):
#         assert howManySquares(966) == 3
#         print("PASSED: howManySquares(966) should return 3")
#
#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
#     print("Nice job, 3/3 tests passed!")
