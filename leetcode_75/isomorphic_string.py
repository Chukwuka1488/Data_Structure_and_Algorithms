"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""
import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_set1, hash_set2 = {}, {}

        for i in range(len(s)):
            if s[i] in hash_set1 and hash_set1[s[i]] != t[i]:
                return False
            elif t[i] in hash_set2 and hash_set2[t[i]] != s[i]:
                return False
            else:
                hash_set1[s[i]] = t[i]
                hash_set2[t[i]] = s[i]
        return True


class TestIsomorphic(unittest.TestCase):
    def test1(self):
        foo = Solution()
        self.assertEqual(foo.isIsomorphic('egg', 'add'), True)
        print("The search insert method of 'isIsomorphic('egg', 'add')' returns True")

    def test2(self):
        foo = Solution()
        self.assertEqual(foo.isIsomorphic('foo', 'bar'), False)
        print("The search insert method of 'isIsomorphic('foo', 'bar')' returns False")

    def test3(self):
        foo = Solution()
        self.assertEqual(foo.isIsomorphic('paper', 'title'), True)
        print("The search insert method of 'isIsomorphic('paper', 'title')' returns True")

    def test4(self):
        foo = Solution()
        self.assertEqual(foo.isIsomorphic('badc', 'baba'), False)
        print("The search insert method of 'isIsomorphic('badc', 'baba')' returns False")
    #
    # def test5(self):
    #     foo = Solution()
    #     self.assertEqual(foo.isIsomorphic([1, 1, 3, 3, 5, 5, 6, 6, 9, 21, 34, 67, 89], 58), 11)
    #     print(
    #         "The search insert method of 'isIsomorphic([1, 1, 3, 3, 5, 5, 6, 6, 9, 21, 34, 67, 89], 58)' "
    #         "returns index = 11")
    #
    # def test6(self):
    #     foo = Solution()
    #     self.assertEqual(foo.isIsomorphic([1, 3, 5, 6], 0), 0)
    #     print(
    #         "The search insert method of 'isIsomorphic([1, 3, 5, 6], 0)' "
    #         "returns index = 0")
    #
    # def test7(self):
    #     foo = Solution()
    #     self.assertEqual(foo.isIsomorphic([1, 3], 2), 1)
    #     print(
    #         "The search insert method of 'isIsomorphic([1, 3], 2)' "
    #         "returns index = 1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice Job! All 3/3 tests passed.")
