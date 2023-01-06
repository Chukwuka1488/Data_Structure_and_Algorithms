# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    bad = 4
    if version == bad:
        return True
    return False


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


print(isBadVersion(4))
foo = Solution()
print(foo.firstBadVersion(5))
