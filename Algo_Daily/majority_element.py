import unittest
from math import floor

import running_time


def majority_element(arr):
    """
    method 1
    :param arr:
    :return: number
    """
    # arr.sort()
    # # idx = floor(len(arr) / 2)
    # # val = arr[idx]
    # # return val
    """
    method 2: My solution
    :param arr: 
    :return: max value in hash set
    """
    # sort the array
    arr.sort()
    # create empty hash map
    hash_set = {}
    while len(arr) > 0:
        hash_set[arr[0]] = arr.count(arr[0])
        # remove all occurrences after counting
        del arr[0:hash_set[arr[0]]]
    return max(hash_set, key=hash_set.get)

    """
      method 3
      :param arr: 
      :return: number
      """
    # hash_set = {}
    # # we keep a local max variable to track what
    # # element is in the majority
    # maximum, val = 0, None
    #
    # for i in range(0, len(arr)):
    #     # increment or initialize the num as a key
    #     if arr[i] in hash_set:
    #         hash_set[arr[i]] += 1
    #     else:
    #         hash_set[arr[i]] = 1
    #
    #     if hash_set[arr[i]] > maximum:
    #         maximum = hash_set[arr[i]]
    #         val = arr[i]
    #
    # return val


# class Test(unittest.TestCase):
#     def test_1(self):
#         assert callable(majority_element) == True
#         print("PASSED: 'majority_element' is a function")
#
#     def test_2(self):
#         assert majority_element([1, 4, 2, 4, 4, 3, 4]) == 4
#         print("PASSED: 'majority_element([1, 4, 2, 4, 4, 3, 4])' should return '4'")
#
#     def test_3(self):
#         assert majority_element([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]) == 1
#         print(
#             "PASSED: 'majority_element([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1])' should return '1'"
#         )


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    # x = generate_random_array.generate_array(100_000)
    print(majority_element([1, 1, 1, 4, 2, 9, 9, 9, 9, 9, 9, 9, 4, 4, 3, 1, 1, 1]))
    # print("Nice job, 3/3 tests passed!")
    running_time.time_to_run()
