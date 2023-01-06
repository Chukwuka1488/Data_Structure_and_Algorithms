"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        val = str(n)
        product = 1
        sum = 0
        for digits in val:
            product *= int(digits)
            sum += int(digits)
        return product - sum


sol = Solution()
print(sol.subtractProductAndSum(234))
