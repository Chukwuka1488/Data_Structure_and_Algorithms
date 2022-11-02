"""
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] +
nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1,
the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
"""

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # find the sum of the arr
        total = sum(nums)
        # set leftside as 0
        left_side = 0
        # check if sum of left side equals sum - leftside - current idx value
        for i in range(len(nums)):
            if left_side == (total - left_side - nums[i]):
                return i
            left_side += nums[i]
        # if condition not met
        return -1
