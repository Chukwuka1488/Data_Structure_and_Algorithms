"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import running_time


def compute(n, m):
    ans = max(i * j
              for i in range(n, m)
              for j in range(n, m)
              if str(i * j) == str(i * j)[:: -1])
    return ans


if __name__ == "__main__":
    print(compute(100, 1000))
    running_time.time_to_run()
