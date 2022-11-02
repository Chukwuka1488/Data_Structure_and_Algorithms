"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import running_time


def primes_method(n):
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] and sieve[p] % 2 == 1:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


if __name__ == '__main__':
    print(sum(primes_method(2_000_000)))
    running_time.time_to_run()
