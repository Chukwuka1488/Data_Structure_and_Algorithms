"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at
that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the
products.
"""


# using brute force
# def get_products_of_all_ints_except_at_index(arr):
#     n = len(arr)
#     res = []
#     for i in range(n):
#         prod = 1
#         val = arr[:i] + arr[i + 1:]
#         for j in val:
#             prod *= j
#         res.append(prod)
#
#     return res

# using dp
def get_products_of_all_ints_except_at_index(arr):
    # get length of given array
    n = len(arr)
    # create an array for dp
    res = [1] * n
    # run an iteration to get the product in the right direction
    for i in range(1, n):
        res[i] = res[i - 1] * arr[i - 1]
    prod = 1
    # run an iteration to get the product in the bvackward direction
    for i in range(n - 2, -1, -1):
        prod *= arr[i + 1]
        res[i] *= prod
    return res


print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
