"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # temp = 0
        if len(nums) == 0:
            return 0
        while left < right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                # temp = mid
            else:
                left = mid + 1
                # temp = mid
        return left + 1 if nums[left] < target else left


import unittest


class Test(unittest.TestCase):
    def test1(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 3, 5, 6], 5), 2)
        print("The search insert method of 'searchInsert([1, 3, 5, 6], 5)' returns index = 2")

    def test2(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 3, 5, 6], 2), 1)
        print("The search insert method of 'searchInsert([1, 3, 5, 6], 2)' returns index = 1")

    def test3(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 3, 5, 6], 7), 4)
        print("The search insert method of 'searchInsert([1, 3, 5, 6], 7)' returns index = 4")

    def test4(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([], 5), 0)
        print("The search insert method of 'searchInsert([], 5)' returns index = 0")

    def test5(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 1, 3, 3, 5, 5, 6, 6, 9, 21, 34, 67, 89], 58), 11)
        print(
            "The search insert method of 'searchInsert([1, 1, 3, 3, 5, 5, 6, 6, 9, 21, 34, 67, 89], 58)' "
            "returns index = 11")

    def test6(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 3, 5, 6], 0), 0)
        print(
            "The search insert method of 'searchInsert([1, 3, 5, 6], 0)' "
            "returns index = 0")

    def test7(self):
        foo = Solution()
        self.assertEqual(foo.searchInsert([1, 3], 2), 1)
        print(
            "The search insert method of 'searchInsert([1, 3], 2)' "
            "returns index = 1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice Job! All 4/4 tests passed.")
