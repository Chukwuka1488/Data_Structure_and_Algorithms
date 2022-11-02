"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

start_time = time.time()


def compute(max_number):
    all_multiples = [i for i in range(max_number) if i % 3 == 0 or i % 5 == 0]
    answer = sum(all_multiples)
    return answer
    # ans = sum(x for x in range(max_number) if (x % 3 == 0 or x % 5 == 0))
    # return str(ans)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(compute(1_000_000_000))
    print("--- %s seconds ---" % (time.time() - start_time))
