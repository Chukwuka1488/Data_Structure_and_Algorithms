# from fractions import gcd
import math
from functools import reduce

import running_time


#
# def generalizedGCD(num, arr):
#
#     return math.gcd(*arr)

def gcd(num, my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


if __name__ == "__main__":
    new_arr = [2, 3, 4, 5, 6]
    val = len(new_arr)

    print(gcd(val, new_arr))
    running_time.time_to_run()
