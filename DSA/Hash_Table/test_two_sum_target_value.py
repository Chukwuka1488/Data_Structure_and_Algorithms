# !python -m unittest two_sum_target_value.py
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:29:14 2022

@author: Chukwuka
"""
from two_sum_target_value import *
# import running_time
import unittest


class TestTwoSum(unittest.TestCase):
    # check for input and output
    def test_volume(self):
        self.assertAlmostEqual(two_sum([2, 7], 9), [0, 1])
        self.assertAlmostEqual(two_sum([2, 7, 3, -1, 4], 2), [2, 3])
        self.assertAlmostEqual(two_sum([2, 7, 3, -1, 4], 100), [])
        self.assertAlmostEqual(two_sum([25], 25), [])
        self.assertAlmostEqual(two_sum([], 10), [])

    # check for type error
    def test_input_value(self):
        self.assertRaises(TypeError, two_sum, True)


if __name__ == '__main__':
    unittest.main()
