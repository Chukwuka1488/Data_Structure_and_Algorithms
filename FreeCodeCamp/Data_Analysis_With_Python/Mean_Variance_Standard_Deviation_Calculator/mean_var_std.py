import numpy as np


#
# # define Python user-defined exceptions
# class MyError(Exception):
#     "Raised when the list of elements is more than or less than 9"
#     pass


def calculate(lst):
    # try:
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # Convert the input list into a 3x3 Numpy array
        arr = np.array(lst).reshape(3, 3)

    # Calculate summary statistics
    mean = arr.mean()
    variance = arr.var()
    std = arr.std()
    max_val = arr.max()
    min_val = arr.min()
    sum_val = arr.sum()

    # Calculate summary statistics along each axis
    col_mean = arr.mean(axis=0).tolist()
    row_mean = arr.mean(axis=1).tolist()
    row_variance = arr.var(axis=1).tolist()
    col_variance = arr.var(axis=0).tolist()
    row_std = arr.std(axis=1).tolist()
    col_std = arr.std(axis=0).tolist()
    row_max = arr.max(axis=1).tolist()
    col_max = arr.max(axis=0).tolist()
    row_min = arr.min(axis=1).tolist()
    col_min = arr.min(axis=0).tolist()
    row_sum = arr.sum(axis=1).tolist()
    col_sum = arr.sum(axis=0).tolist()

    # Flatten the array and calculate summary statistics
    flat_arr = arr.flatten()
    flat_mean = flat_arr.mean()
    flat_variance = flat_arr.var()
    flat_std = flat_arr.std()
    flat_max = flat_arr.max()
    flat_min = flat_arr.min()
    flat_sum = flat_arr.sum()

    # Create a dictionary containing all of the calculated summary statistics
    calculations = {
        "mean": [col_mean, row_mean, flat_mean],
        "variance": [col_variance, row_variance, flat_variance],
        "standard deviation": [col_std, row_std, flat_std],
        "max": [col_max, row_max, flat_max],
        "min": [col_min, row_min, flat_min],
        "sum": [col_sum, row_sum, flat_sum],
    }

    return calculations


# except ValueError as e:
#     return e


matrix = [0, 1, 2, 3, 4, 5, 7, 8]
summary = calculate(matrix)
print(summary)
