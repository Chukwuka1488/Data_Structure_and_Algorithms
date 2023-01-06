from typing import List

import running_time


class Solution(object):
    def __init__(self):
        self.arr = None

    def single_lonely_number(self, arr: List[int]) -> int:
        # self.arr = arr
        # self.arr.sort()
        # while len(set(self.arr)) != len(self.arr):
        #     if self.arr.count(self.arr[0]) > 1:
        #         del arr[0:self.arr.count(self.arr[0])]
        #     else:
        #         self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        # return self.arr[0]

        """
        :param arr: array of int
        :return: int
        """
        # get unique values in arr
        new_arr = list(set(self.arr))
        for i in new_arr:
            if self.arr.count(i) == 1:
                return i
        return -1


if __name__ == "__main__":
    foo = Solution()
    print(foo.single_lonely_number([4, 4, 6, 1, 3, 1, 3]))
    running_time.time_to_run()
