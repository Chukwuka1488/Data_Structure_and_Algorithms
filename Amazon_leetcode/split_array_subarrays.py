"""
Suppose we have an array called nums, we have to find the number of good ways to split this array nums.
Answer may be too large so return result modulo 10^9 + 7. Here a split of an array (with integer elements) is
good if the array is split into three non-empty contiguous subarrays respectively from left to right, and the
sum of the elements in left side is less than or equal to the sum of the elements in mid part, and the sum of the
elements in mid-part is less than or equal to the sum of the elements in right.

So, if the input is like nums = [2,3,3,3,7,1], then the output will be 3 because there are three different ways of
splitting,

[2],[3],[3,3,7,1]
[2],[3,3],[3,7,1]
[2,3],[3,3],[7,1]
"""


def solve(nums):
    n, m = len(nums), 10 ** 9 + 7
    ss = [0] * (1 + n)
    for i, val in enumerate(nums, 1):
        ss[i] = ss[i - 1] + val

    r = rr = ans = 0
    for l in range(1, n - 1):
        r = max(r, l + 1)
        while r < n - 1 and ss[r] - ss[l] < ss[l]:
            r += 1
        rr = max(rr, r)
        while rr < n - 1 and ss[n] - ss[rr + 1] >= ss[rr + 1] - ss[l]:
            rr += 1
        if ss[l] > ss[r] - ss[l]:
            break
        if ss[r] - ss[l] > ss[n] - ss[r]:
            continue
        ans = (ans + rr - r + 1) % m
    return ans


if __name__ == "__main__":
    arr = [1, 3, 2, 4, 5]
    print(solve(arr))
