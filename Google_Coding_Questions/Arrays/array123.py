"""

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""


def array123(nums):
    # loop through the array starting from the 3rd value index 2 and compare the value to desired value
    for i in range(2, len(nums)):
        if (nums[i - 2], nums[i - 1], nums[i]) == (1, 2, 3):
            return True
    return False


print(array123([1, 1, 2, 1, 2, 3]))
