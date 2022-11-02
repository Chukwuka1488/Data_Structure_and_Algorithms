from typing import List

import running_time


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        hx = set()
        for i in nums:
            if i in hx:
                return True
            hx.add(i)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1, 2, 3]))
    running_time.time_to_run()
