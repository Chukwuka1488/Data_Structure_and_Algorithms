"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
from typing import List
from itertools import combinations


# def get_combinations(arr, number):
#     # create a list to store the combinations
#     combinations = []
#
#     # generate combinations iteratively
#     for i in range(len(arr)):
#         # if combination = 4 add it to the list
#         if i + number <= len(arr):
#             combinations.append(arr[i:i + number])
#
#     return combinations


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #     # set variables for number of elements in array combinations,
        #     # count to serve as key for hash map
        #     # lst to serve as the initialized hash map
        #     number, count, lst = 4, 0, {}
        #     # use itertools to get all combinations possible
        #     # run a loop to check if sum of arrays is equal to target
        #     new_new_arr = [sorted(list(i)) for i in combinations(nums, number)]
        #     print(new_new_arr)
        #     for i in new_new_arr:
        #         if sum(i) == target and i not in lst.values():
        #             # if true, increment count and sort array to avoid duplicates
        #             count = count + 1
        #             lst[count] = i
        #
        #     return list(lst.values())

        # ******************************************** final solution ******************************************
        # Sort the array in increasing order,
        # using library function for quick sort
        nums.sort()
        a = []

        # Now fix the first 2 elements one by one and find the other two elements
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):

                # initialize the two variables as indexes of the first and last elements in the remaining elements
                left = j + 1
                right = n - 1

                # to find the remaining two elements , move the index variables (left & right) toward each other
                while left < right:
                    if nums[i] + nums[j] + nums[right] + nums[left] == target:
                        ans = [nums[i], nums[j], nums[right], nums[left]]
                        a.append(ans)
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[right] + nums[left] < target:
                        left += 1
                    else:
                        right -= 1
        # a = [i for i in a]
        b = []
        for i in range(1, len(a)):
            if a[i-1] == a[i]:
                del a[i-1]
            b.append(a[i-1])


        return a


sol = Solution()
values = [2, 2, 2, 2, 2]
target = 8
print(sol.fourSum(values, target))
