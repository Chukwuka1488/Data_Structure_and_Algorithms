import random

import numpy as np


def generate_array(n):
    rand_nums = np.random.randint(-1000000000, 1000000000, n)
    return rand_nums
    # return [random.random() for _ in range(n)]


if __name__ == "__main__":
    (generate_array(100_000))
