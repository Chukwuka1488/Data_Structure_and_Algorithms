# A dynamic programming based Python
# program to find minimum number of
# squares whose sum is equal to a
# given number


# Returns count of minimum squares
# that sum to n
def getMinSquares(n):
    # set the range of n to -1 or a base case
    cache = [0, 1, 2, 3]

    for i in range(4, n + 1):
        cache.append(i)
        for j in range(1, int(i ** 0.5) + 1):
            # set temp value
            temp = j ** 2
            if temp > i:
                break
            # set the first one as value at index i
            a = cache[i]
            # set the second parameters as value at index [(i - j**2) + 1]
            b = cache[i - temp] + 1
            cache[i] = min(a, b)

    return cache[n]


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert getMinSquares(16) == 1
        print("PASSED: howManySquares(16) should return 1")

    def test_2(self):
        assert getMinSquares(12) == 3
        print("PASSED: howManySquares(12) should return 3")

    def test_3(self):
        assert getMinSquares(966) == 3
        print("PASSED: howManySquares(966) should return 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
