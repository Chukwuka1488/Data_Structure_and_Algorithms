"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This
also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List


class Solution(object):
    def pivotIndex(self, nums: List[int]) -> int:
        # find sums of the arr
        S = sum(nums)
        # set left sum at 0
        leftsum = 0
        for i in range(len(nums)):
            # check if leftsum equals right sum and return index
            if leftsum == (S - leftsum - nums[i]):
                return i
            leftsum += nums[i]
        return -1


if __name__ == "__main__":
    foo = Solution()
    num = [2, 1, -1]
    print(foo.pivotIndex(num))
