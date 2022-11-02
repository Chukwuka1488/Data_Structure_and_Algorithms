"""
You are given an array of integers and another integer targetValue. Write a function that will take this inputs and
return the indices of the 2 integers in the array that add up to the target value
"""

# import running_time

"""
Method 1: Brute force method
time complexity: double for loop leads to O(n**2) 
space complexity: is O(1) as we do not store values anywhere
"""

# def two_sum(arr, n):
#     if len(arr) <= 1:
#         return list()
#
#     for i in range(len(arr)):
#         for j in range(1, len(arr)):
#             if arr[i] + arr[j] == n:
#                 return [i, j]
#     else:
#         return []


"""
Method 2: Using hash table 
time complexity: O(n) as we traverse the array only once
space complexity: O(n)
"""


def two_sum(arr, n):
    # dictionary to store values
    hash_table = {}
    for i in range(len(arr)):
        needed_value = n - arr[i]
        if needed_value in hash_table:
            return [hash_table[needed_value], i]
        else:
            hash_table[arr[i]] = i
    return []


print(two_sum([2, 7], 9))
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
