"""
Given an integer array nums, move all the even integers to the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        num = sorted(nums)
        for i in num:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        # even.extend(odd)
        return even + odd


import unittest


class TestSortArrayByParity(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.sortArrayByParity([]), [])

    def test_single_element(self):
        self.assertEqual(self.solution.sortArrayByParity([5]), [5])
        self.assertEqual(self.solution.sortArrayByParity([-5]), [-5])

    def test_two_elements(self):
        self.assertEqual(self.solution.sortArrayByParity([5, 7]), [5, 7])
        self.assertEqual(self.solution.sortArrayByParity([-5, 5]), [-5, 5])
        self.assertEqual(self.solution.sortArrayByParity([5, 5]), [5, 5])
        self.assertEqual(self.solution.sortArrayByParity([-5, -5]), [-5, -5])

    def test_three_elements(self):
        self.assertEqual(self.solution.sortArrayByParity([5, 7, 3]), [3, 5, 7])
        self.assertEqual(self.solution.sortArrayByParity([-5, 5, 0]), [0, -5, 5])
        self.assertEqual(self.solution.sortArrayByParity([5, 5, 5]), [5, 5, 5])
        self.assertEqual(self.solution.sortArrayByParity([-5, -5, -5]), [-5, -5, -5])

    def test_even_number_of_elements(self):
        self.assertEqual(self.solution.sortArrayByParity([5, 7, 3, 8]), [8, 3, 5, 7])
        self.assertEqual(self.solution.sortArrayByParity([-5, 5, 0, -10]), [-10, 0, -5, 5])
        self.assertEqual(self.solution.sortArrayByParity([5, 5, 5, 5]), [5, 5, 5, 5])


    def test_odd_number_of_elements(self):
        self.assertEqual(self.solution.sortArrayByParity([5, 7, 3, 8, 2]), [2, 8, 3, 5, 7])
        self.assertEqual(self.solution.sortArrayByParity([-5, 5, 0, -10, 100]), [-10, 0, 100, -5, 5])
        self.assertEqual(self.solution.sortArrayByParity([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])
        self.assertEqual(self.solution.sortArrayByParity([-5, -5, -5, -5, -5]), [-5, -5, -5, -5, -5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Passed All Tests!")
