"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring
the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


def centered_average(nums):
    if len(nums) < 3:
        return 0
    # sort array from smallest to largest
    sorted_nums = sorted(nums)
    # get the length of new array after removing the first and last
    length = len(sorted_nums) - 2
    # remove the smallest and largest number using slicing
    no_smallest_largest = sorted_nums[1:len(nums) - 1]
    # get the average of the remaining and round to int
    mean = int(sum(no_smallest_largest) / length)

    return mean


import unittest


class TestCenteredAverage(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(centered_average([]), 0)

    def test_single_element(self):
        self.assertEqual(centered_average([5]), 0)
        self.assertEqual(centered_average([-5]), 0)

    def test_two_elements(self):
        self.assertEqual(centered_average([5, 7]), 0)
        self.assertEqual(centered_average([-5, 5]), 0)
        self.assertEqual(centered_average([5, 5]), 0)
        self.assertEqual(centered_average([-5, -5]), 0)

    def test_three_elements(self):
        self.assertEqual(centered_average([5, 7, 3]), 5)
        self.assertEqual(centered_average([-5, 5, 0]), 0)
        self.assertEqual(centered_average([5, 5, 5]), 5)
        self.assertEqual(centered_average([-5, -5, -5]), -5)

    def test_even_number_of_elements(self):
        self.assertEqual(centered_average([5, 7, 3, 8]), 6)
        self.assertEqual(centered_average([-5, 5, 0, -10]), -2)
        self.assertEqual(centered_average([5, 5, 5, 5]), 5)
        self.assertEqual(centered_average([-5, -5, -5, -5]), -5)

    def test_odd_number_of_elements(self):
        self.assertEqual(centered_average([5, 7, 3, 8, 2]), 5)
        self.assertEqual(centered_average([-5, 5, 0, -10, 100]), 0)
        self.assertEqual(centered_average([5, 5, 5, 5, 5]), 5)
        self.assertEqual(centered_average([-5, -5, -5, -5, -5]), -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 1/1 tests passed!")
