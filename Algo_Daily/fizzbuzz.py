import sys
import unittest

import running_time


def fizz_buzz(n):
    arr = ("fizzbuzz" if x % 3 == 0 and x % 5 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x) for x
           in range(1, n + 1))
    print('***********************')
    print(f"byte size: {sys.getsizeof(arr) / 1_000_000:.2f} MB")
    print('***********************')
    value = ""
    for expression in arr:
        value += expression
    # arr = ""
    # def f(x): return "fizzbuzz" if x % 3 == 0 and x % 5 == 0 else (
    #     "fizz" if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x))

    # for i in range(1, n + 1):
    #     arr += f(i)
    # return "".join(arr)

    return value


class Test(unittest.TestCase):
    def test_1(self):
        assert fizz_buzz(0) == ""
        print("PASSED: Expect fizz_buzz(0) to equal ''")

    def test_2(self):
        assert fizz_buzz(1) == "1"
        print("PASSED: Expect fizz_buzz(1) to equal '1'")

    def test_3(self):
        assert fizz_buzz(15) == "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz"
        print(
            "PASSED: Expect fizz_buzz(15) to equal '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
    running_time.time_to_run()
