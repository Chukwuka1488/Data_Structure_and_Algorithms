from typing import List


class Solution:
    def __init__(self):
        self.nums = None

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums

        self.nums.sort()

        return self.nums[-k]
#         if not nums: return
#         pivot = random.choice(nums)
#         left =  [x for x in nums if x > pivot]
#         mid  =  [x for x in nums if x == pivot]
#         right = [x for x in nums if x < pivot]

#         L, M = len(left), len(mid)

#         if k <= L:
#             return self.findKthLargest(left, k)
#         elif k > L + M:
#             return self.findKthLargest(right, k - L - M)
#         else:
#             return mid[0]
