"""
Given a string S, the task is to find out the minimum no of adjacent swaps required to make string s palindrome.
If it is not possible, then return -1.
"""
from itertools import groupby


def all_equal(lst):
    return any(sum(1 for _ in g) > 1 for _, g in groupby(lst))


def minSwap(s):
    strng = list(s)
    unmp = {}
    for i in strng:
        unmp[i] = unmp.get(i, 0) + 1
    odd = 0
    result = 0
    left = 0
    right = len(strng) - 1
    for i in unmp:
        if unmp[i] % 2 != 0:
            odd += 1
    # If we found more then one odd number
    if odd > 1:
        return -1
    while left < right:
        l = left
        r = right
        while strng[l] != strng[r]:
            r -= 1
        if l == r:
            # When we found odd element move towards middle
            strng[r], strng[r + 1] = strng[r + 1], strng[r]
            result += 1
            continue
        else:
            # Normal element  move towards right of string
            while r < right:

                b = strng[r + 1]
                if r < right - 1:
                    c = strng[r + 2]
                else:
                    c = None
                if b == c and c != None:
                    strng[r], strng[r + 1] = strng[r + 1], strng[r]
                    r += 1
                    # result += 0
                else:
                    strng[r], strng[r + 1] = strng[r + 1], strng[r]
                    r += 1
                    result += 1
        left += 1
        right -= 1
    return result


s = "0100101"
print(minSwap(s))
print(s[2:3])
print(all_equal([1,1,1]))
