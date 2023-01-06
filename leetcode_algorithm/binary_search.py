"""
0 (quiet): you just get the total numbers of tests executed and the global result
1 (default): you get the same plus a dot for every successful test or an F for every failure
2 (verbose): you get the help string of every test and the result
"""
import unittest


def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # get middle value of arr
        mid = left + (right - left) // 2

        # check if value exists at mid
        if value == arr[mid]:
            return mid
        # if value is less than mid value , move mid value leftward
        elif value < arr[mid]:
            right = mid - 1
        # if value is less than mid value , move mid value rightward
        else:
            left = mid + 1

    return -1


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 110), 10)
        print(
            "The binary search method 'binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 110)' "
            "should return index = 10")

    def test2(self):
        self.assertEqual(binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 140), -1)
        print(
            "The binary search method 'binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 140)' "
            "should return index = -1")

    def test3(self):
        self.assertEqual(binary_search([], 140), -1)
        print("The binary search method 'binary_search([], 140)' should return index = -1")

    def test4(self):
        self.assertEqual(binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 40), 3)
        print(
            "The binary search method 'binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130], 140)' "
            "should return index = 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("PASSED: 4/4 test passed.")
