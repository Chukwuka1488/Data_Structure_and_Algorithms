"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will
represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
"""


def FindIntersection(strArr):
    # check for base case
    if strArr[0] == "" or strArr[1] == "":
        return ""
    # get the fist and second element of the array
    # split by comma, store in an array and convert to integer
    # run a set function to get only unique values
    first = set([int(i) for i in strArr[0].split(',')])
    second = set([int(i) for i in strArr[1].split(',')])

    # use the python intersection module snd sort it
    intersect = sorted(list(first.intersection(second)))
    int_str = [str(i) for i in intersect]

    return ','.join(int_str)


import unittest


class Test(unittest.TestCase):
    def test_empty_sets(self):
        self.assertEqual(FindIntersection([" ", ""]), "")
        self.assertEqual(FindIntersection(["1,2,3", ""]), "")
        self.assertEqual(FindIntersection(["", "4,5,6"]), "")

    def test_no_intersection(self):
        self.assertEqual(FindIntersection(["1,2,3", "4,5,6"]), "")
        self.assertEqual(FindIntersection(["1,3,5", "2,4,6"]), "")

    def test_intersection(self):
        self.assertEqual(FindIntersection(["1,2,3", "3,4,5"]), "3")
        self.assertEqual(FindIntersection(["1,2,3,4", "3,4,5,6"]), "3,4")
        self.assertEqual(FindIntersection(["1,2,3", "1,2,3"]), "1,2,3")

    def test_unsorted_sets(self):
        self.assertEqual(FindIntersection(["3,1,2", "3,4,5"]), "3")
        self.assertEqual(FindIntersection(["1,3,5", "2,4,6"]), "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print("Nice job, 10/10 tests passed!")
