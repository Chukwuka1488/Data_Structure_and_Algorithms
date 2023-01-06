"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will
represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
"""


def FindIntersection(strArr):
    first = set([int(i) for i in strArr[0].split(',')])
    second = set([int(i) for i in strArr[1].split(',')])

    intersect = sorted(list(first.intersection(second)))
    int_str = [str(i) for i in intersect]

    return ','.join(int_str)


# keep this function call here
print(FindIntersection(input()))
