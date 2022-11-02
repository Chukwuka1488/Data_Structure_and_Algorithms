from itertools import accumulate
from typing import List
import unittest

import running_time


class Solution:
    def __init__(self):
        self.nums = None

    def running_sums(self, nums: List[int]) -> List[int]:
        self.nums = nums
        # return list(accumulate(self.nums))
        value = 0
        arr = []
        for i in range(len(self.nums)):
            value += self.nums[i]
            arr.append(value)
        return arr


class Test(unittest.TestCase):
    def test1(self):
        bar = Solution()
        self.assertListEqual(list(bar.running_sums([1, 2, 3, 4, 5])), [1, 3, 6, 10, 15], "true")
        print("PASSED: the running sum of running_sums([1, 2, 3, 4, 5]) equals [1, 3, 6, 10, 15]")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice Job, 1/1 tests passed")
    # bar = Solution()
    # x = bar.running_sums([1, 2, 3, 4, 5])
    # print(x)
    # print(type(x))
    running_time.time_to_run()
