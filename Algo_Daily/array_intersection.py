"""
Can you write a function that takes two arrays as inputs and returns to us their intersection? We can call the
method intersection. Let's return the intersection of the two inputs in the form of an array. As a reminder, the
definition of an intersection of two sets A and B is the set containing all elements of A that also belong to B
(or equivalently, all elements of B that also belong to A).

Methods to solve:
Brute Force: O(n**2)
Hash_Maps Maps: O()
"""

import unittest

import running_time


def arr_intersection(arr1, arr2):
    arr_1 = set(arr1)
    arr_2 = set(arr2)

    arr_final = list(arr_1.intersection(arr_2))
    return arr_final


class Test(unittest.TestCase):
    def test_1(self):
        assert arr_intersection([6, 0, 12, 10, 16], [3, 15, 18, 20, 15]) == []
        print(
            "PASSED: `intersection([6,0,12,10,16],[3,15,18,20,15])` should return `[]`"
        )

    def test_2(self):
        assert arr_intersection([1, 5, 2, 12, 6], [13, 10, 9, 5, 8]) == [5]
        print("PASSED: `intersection([1,5,2,12,6],[13,10,9,5,8])` should return `[5]`")

    def test_3(self):
        assert arr_intersection([3], [15]) == []
        print("PASSED: `intersection([3],[15])` should return `[]`")

    def test_4(self):
        assert arr_intersection([2, 16, 8, 9], [14, 15, 2, 20]) == [2]
        print("PASSED: `intersection([2,16,8,9],[14,15,2,20])` should return `[2]`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
