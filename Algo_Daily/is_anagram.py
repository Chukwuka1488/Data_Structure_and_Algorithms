import unittest


def is_anagram(str1, str2):
    a = list(str1)
    b = list(str2)

    a.sort()
    b.sort()

    return a == b


class Test(unittest.TestCase):
    def test_1(self):
        assert is_anagram("Mary", "Army") == False
        print("PASSED: is_anagram('Mary', 'Army') should return False")

    def test_2(self):
        assert is_anagram("cinema", "iceman") == True
        print("PASSED: is_anagram('cinema', 'iceman') should return True")

    def test_3(self):
        assert is_anagram("jake", "jay") == False
        print("PASSED: is_anagram('jake', 'jay') should return False")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
