#!/bin/python3


import os


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Refactor this code
def hour_glass_sum(arr):
    # Initialize maximum hourglass sum as minimum value
    max_hourglass = -999999999999

    # Iterate through each element in the array
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            # Calculate the sum of the current hourglass
            hourglass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]
            # Update the maximum hourglass sum if necessary
            max_hourglass = max(max_hourglass, hourglass_sum)

    return max_hourglass


if __name__ == '__main__':
    # arr = []
    #
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # print(arr)

    arr_2d = [[-9, -9, -9, 1, 1, 1],
              [0, -9, 0, 4, 3, 2],
              [-9, -9, -9, 1, 2, 3],
              [0, 0, 8, 6, 6, 0],
              [0, 0, 0, -2, 0, 0],
              [0, 0, 1, 2, 4, 0]]

    print(hourglassSum(arr_2d))
