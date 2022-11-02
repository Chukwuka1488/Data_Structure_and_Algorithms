"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 3025
Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import running_time


def compute(n):
    sum_of_squares = sum(i * i for i in range(1, n + 1))
    square_of_the_sum = pow(sum(i for i in range(1, n + 1)), 2)
    return square_of_the_sum - sum_of_squares


if __name__ == '__main__':
    print(compute(100))
    running_time.time_to_run()
