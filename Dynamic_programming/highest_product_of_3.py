"""
Given an array of integers, find the highest product you can get from three of the integers.

The input arrayOfInts will always have at least three integers.
"""
"""
time complexity = O(NlogN) because of using the sort function
space complexity = O(NlogN) because of using the sort function
"""

# def highest_product_of_three(nums):
#     n = len(nums)
#     nums.sort()
#     max_prod = float('-inf')
#     max_prod = max(max_prod, nums[0] * nums[1] * nums[n - 1])
#     max_prod = max(max_prod, nums[n - 1] * nums[n - 2] * nums[n - 3])
#     return max_prod

"""
time complexity = O(N) because of using the sort function
space complexity = O(1) because of using the sort function
"""


def highest_product_of_three(nums):
    n = len(nums)
    min_1 = float('inf')
    min_2 = float('inf')
    max_1 = float('-inf')
    max_2 = float('-inf')
    max_3 = float('-inf')

    for i in range(n):
        if nums[i] <= min_1:
            min_2 = min_1
            min_1 = nums[i]
        elif nums[i] <= min_2:
            min_2 = nums[i]
        if nums[i] >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = nums[i]
        elif nums[i] >= max_2:
            max_3 = max_2
            max_2 = nums[i]
        elif nums[i] >= max_3:
            max_3 = nums[i]

    return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)


print(highest_product_of_three([-5, -7, 4, 2, 1, 9]))
