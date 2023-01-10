"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when
everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as an object of a
Meeting class with integer variables startTime and endTime. These integers represent the number of 30-minute blocks past 9:00am.
"""


def meeting(arr_2d):
    # Sorting based on the increasing order
    # of the start intervals
    arr_2d.sort(key=lambda x: x[0])
    # Stores index of last element
    # in output array (modified arr[])
    index = 0

    for i in range(1, len(arr_2d)):
        a = arr_2d[index][1]
        b = arr_2d[i][0]
        if a >= b:
            arr_2d[index][1] = max(arr_2d[index][1], arr_2d[i][1])
        else:
            index = index + 1
            arr_2d[index] = arr_2d[i]

    for i in range(index + 1):
        print(arr_2d[i], end=" ")


arr = [[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]
meeting(arr)
