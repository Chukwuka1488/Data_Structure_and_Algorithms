"""
You are given 2 strings. Write a function that will check if these two strings are isomorphic.
"""

# import running_time

"""
Method 1: Brute force method
time complexity: double for loop leads to O(n**2) 
space complexity: is O(1) as we do not store values anywhere
"""


def isomorphic_strings(a, b):
    if len(a) != len(b):
        return False
    aa = list(a)
    bb = list(b)
    a_hash = {}
    b_hash = {}

    for i in range(len(aa)):
        if aa[i] not in a_hash:
            a_hash[aa[i]] = bb[i]
        if bb[i] not in b_hash:
            b_hash[bb[i]] = aa[i]
        if a_hash[aa[i]] != bb[i] or b_hash[bb[i]] != aa[i]:
            return False
    return True


print(isomorphic_strings('greeni', 'spoolo'))

"""
Method 2: Using hash table 
time complexity: O(n) as we traverse the array only once
space complexity: O(n)
"""

# def two_sum(arr, n):
#     # dictionary to store values
#     hash_table = {}
#     for i in range(len(arr)):
#         needed_value = n - arr[i]
#         if needed_value in hash_table:
#             return [hash_table[needed_value], i]
#         else:
#             hash_table[arr[i]] = i
#     return []
#
#
# print(two_sum([2, 7], 9))
# if __name__ == '__main__':
#     x = [1, 2, 3, 4, 6, 7, 8, 9, 3, 12, 6, 4, 23]
#     v = 35
#     # print("brute force start")
#     # running_time.time_to_run()
#     # print(two_sum(x, v))
#     # running_time.time_to_run()
#     # print("brute force end")
#     print("hash table start")
#     running_time.time_to_run()
#     print(two_sum(x, v))
#     running_time.time_to_run()
#     print("hash table end")
