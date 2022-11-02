# !python -m unittest two_sum_target_value.py
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:29:14 2022

@author: Chukwuka
"""
from two_sum_target_value import *

import unittest


class TestTwoSum(unittest.TestCase):
    # check for input and output
    def test_volume(self):
        self.assertAlmostEqual(two_sum('abc', 'pq'), False)
        self.assertAlmostEqual(two_sum('ababr', 'eoeoo'), False)
        self.assertAlmostEqual(two_sum('green', 'spool'), True)
        self.assertAlmostEqual(two_sum('abcdc', 'pqrpo'), False)
        # self.assertAlmostEqual(two_sum([], 10), [])

    # check for type error
    def test_input_value(self):
        self.assertRaises(TypeError, two_sum, True)


if __name__ == '__main__':
    unittest.main()
