from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # if len(nums) == 1 and nums[0] == 0:
        #     return 0
        # if len(nums) == 1 and nums[0] > 0:
        #     return 1
        # nums.sort()
        # count = 0
        # while sum(nums) > 0:
        #     min_num = [i for i in nums if i != 0]
        #     temp = [i - min(min_num) for i in nums if i != 0]
        #     nums = temp
        #     count += 1
        #
        # return count
        a = set(nums)
        b = {0}
        return len(a - b)


foo = Solution()
print(foo.minimumOperations(nums=[1, 5, 0, 3, 5]))
