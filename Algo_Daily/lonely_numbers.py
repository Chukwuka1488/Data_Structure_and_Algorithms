def lonely_number(numbers):
    new_arr = set(numbers)
    if len(numbers) == 1:
        return numbers[0]
    while len(set(numbers)) != len(numbers):
        for i in new_arr:
            if numbers.count(i) == 1:
                return i
    return -1

    # return numbers[0]


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert lonely_number([4, 4, 6, 1, 3, 1, 3]) == 6
        print("PASSED: `lonely_number([4, 4, 6, 1, 3, 1, 3])` should return `6`")

    def test_2(self):
        assert lonely_number([3, 3, 9]) == 9
        print("PASSED: `lonely_number([3, 3, 9])` should return `9`")

    def test_3(self):
        assert callable(lonely_number) == True
        print("PASSED: `lonely_number` is a function")

    def test_4(self):
        assert lonely_number([10]) == 10
        print("PASSED: `lonely_number([10])` should return `10`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
