from typing import List

import running_time


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        n = len(nums)
        d = {}
        w = valueDiff + 1
        for i in range(n):
            m = nums[i] / w
            if m in d:
                print([])
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= indexDiff:
                del d[nums[i - indexDiff] / w]
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([8, 7, 15, 1, 6, 1, 9, 15], 1, 3))
    running_time.time_to_run()
