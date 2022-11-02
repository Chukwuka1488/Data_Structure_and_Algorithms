#!/bin/python3

import math
import os
import random
import re
import sys

import running_time


# get a dictionary of every character as key and count as value
# def counter(word):
#     # word = "100011010"  # word = "1"
#     count = 1
#     length = ""
#     d = {}
#     if len(word) > 1:
#         for i in range(1, len(word)):
#             if word[i - 1] == word[i]:
#                 count += 1
#             else:
#                 updict = {}
#                 length += word[i - 1] + " repeats " + str(count) + ", "
#                 # d[word[i - 1]] = count
#                 updict[word[i - 1]] = count
#                 # x = word[i-1]
#                 # y = (d[x])
#                 # z = (updict[x])
#                 # if word[i - 1] in d and d[word[i - 1]] < count:
#                 #     # res = {key: updict.get(key, d[key]) for key in d}
#                 res = {k: (updict.get(k, d[k]) if v < count else d.setdefault(word[i - 1], count)) for (k, v) in
#                        d.items()}
#                 d = res
#                 # d[word[i - 1]] = count
#                 count = 1
#
#         length += ("and " + word[i] + " repeats " + str(count))
#         d[word[i - 1]] = count
#     else:
#         i = 0
#         length += ("and " + word[i] + " repeats " + str(count))
#         d[word[i - 1]] = count
#     print(d)
#     return length


def counter(word):
    count = 1
    d = {'1': 0, '0': 0}
    if len(word) > 1:
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                count += 1
            else:
                updict = {}
                updict[word[i - 1]] = count
                if word[i - 1] in d and updict[word[i - 1]] >= d[word[i - 1]]:
                    d.update(updict)
                    count = 1
    else:
        i = 0
        d[word[i - 1]] = count
    return d


"""
def two_sum_hash(arr, n):
    # dictionary to store values
    hash_table = {}
    for i in range(len(arr)):
        needed_value = n - arr[i]
        if needed_value in hash_table:
            return [i, hash_table[needed_value]]
        else:
            hash_table[arr[i]] = i
    return []
"""


def bin_num(val):
    x = []
    while val // 2 > 0:
        x.append(val % 2)
        val = val // 2
    x.append(val)
    doc = "".join([str(i) for i in x[::-1]])
    max_ones = counter(doc)
    # list1 = doc.split('0')
    # temp = max(len(i) for i in list1)
    # # print(temp)
    return max_ones


if __name__ == '__main__':
    # n = int(input().strip())
    # print(bin(125))
    n = 375027
    print(bin_num(n))
    running_time.time_to_run()
