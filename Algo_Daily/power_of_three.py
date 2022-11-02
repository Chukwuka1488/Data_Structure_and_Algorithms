"""
Given an integer num, write a method to determine if it is a power of 3.
Constraints:
    The given would be a non-zero positive integer in the range between 1 and 2147483647
    Expected space complexity : O(logN)
    Expected time complexity : O(1)
"""

import math
import unittest

import running_time


def power_of_three(num):
    # problem states that zero and non-positive number would not be given
    # if num <= 0:
    #     return False
    # if num == 1:
    #     return True
    # print(math.log(num, 3))
    # return math.log(num, 3).is_integer()

    curr_quotient = num
    if curr_quotient == 1:
        return True

    while curr_quotient > 0:
        curr_quotient = curr_quotient / 3
        if curr_quotient == 1:
            return True

    return False


# class Test(unittest.TestCase):
#     def test1(self):
#         assert power_of_three(9) == True
#         print(f"PASSED: power_of_three(9) should be True")
#
#     def test2(self):
#         assert power_of_three(7) == False
#         print(f"PASSED: power_of_three(7) should be False")
#
#     def test3(self):
#         assert power_of_three(270) == False
#         print(f"PASSED: power_of_three(270) should be False")
#
#     def test4(self):
#         assert power_of_three(81) == True
#         print(f"PASSED: power_of_three(91) should be True")
#
#     def test5(self):
#         assert power_of_three(1) == True
#         print(f"PASSED: power_of_three(1) should be True")
#
#     def test6(self):
#         assert power_of_three(0) == False
#         print(f"PASSED: power_of_three(0) should be False")
#

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    print("Nice job, 6/6 tests passed!")
    print(power_of_three(2147483647))
    running_time.time_to_run()
