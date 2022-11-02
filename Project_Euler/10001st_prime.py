"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10_001st prime number?
"""
import running_time


def prime(i, primes):
    for prime_num in primes:
        # True
        # 0 as false in python and non-zero values is true
        if not (i == prime_num or i % prime_num):
            return False
    primes.add(i)
    return i


def compute(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p >= n:
                return primes
        i += 1


if __name__ == '__main__':
    exact_value = sorted(list(compute(10001)))
    print(exact_value[-1])
    running_time.time_to_run()


# ******************** Faster Method *****************************
# import eulerlib, itertools
#
#
# # Computers are fast, so we can implement this solution by testing each number
# # individually for primeness, instead of using the more efficient sieve of Eratosthenes.
# #
# # The algorithm starts with an infinite stream of incrementing integers starting at 2,
# # filters them to keep only the prime numbers, drops the first 10000 items,
# # and finally returns the first item thereafter.
# def compute():
#     ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
#     return str(ans)
#
#
# if __name__ == "__main__":
#     print(compute())
#     running_time.time_to_run()
