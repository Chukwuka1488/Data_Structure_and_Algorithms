#!/bin/python3


import os


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_hourglass = -999999999999

    for i, inum in enumerate(arr):
        for j, jnum in enumerate(arr):
            if i < len(arr) - 2 and j < len(arr) - 2:
                hourglass_sum = sum(
                    [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j + 1], arr[i + 2][j], arr[i + 2][j + 1],
                     arr[i + 2][j + 2]])
                if hourglass_sum > max_hourglass:
                    max_hourglass = hourglass_sum

    return max_hourglass


if __name__ == '__main__':
    # arr = []
    #
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # print(arr)

    arr_2d = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0],
              [0, 0, 0, -2, 0, 0],
              [0, 0, 1, 2, 4, 0]]

    print(hourglassSum(arr_2d))
