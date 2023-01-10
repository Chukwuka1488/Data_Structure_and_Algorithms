"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Time complexity: O(n^2 * log(n))
"""
import unittest
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the nums list in ascending order
        nums.sort()

        # Initialize a set to store the unique combinations
        combs = []

        # Loop through the nums list two elements at a time
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Set the left and right pointers to the next elements after i and j
                left = j + 1
                right = len(nums) - 1
                # Loop while the left and right pointers have not crossed each other
                while left < right:
                    # Get the current combination of four elements
                    comb = [nums[i], nums[j], nums[left], nums[right]]
                    comb = sorted(comb)
                    # Calculate the sum of the combination
                    total = sum(comb)
                    # If the sum is equal to the target, add the combination to the set
                    # and move the left and right pointers inward
                    if total == target and comb not in combs:
                        combs.append(comb)
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return combs


# sol = Solution()
# values = [1, 0, -1, 0, -2, 2]
# target = 0
# # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# print(sol.fourSum(values, target))


class TestFourSum(unittest.TestCase):
    def test_four_sum(self):
        # Create an instance of the Solution class
        sol = Solution()

        # Test the fourSum() function with various inputs and targets
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 0), [(-2, -1, 1, 2)])
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 1), [(-2, -1, 0, 2)])
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 2), [(-2, -1, 1, 2)])
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 3), [(-2, -1, 0, 2)])
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 4), [(-2, -1, 1, 2)])


if __name__ == '__main__':
    unittest.main()
