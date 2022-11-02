"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import running_time


# Computers are fast, so we can implement a brute-force search to directly solve the problem.
def compute(sum_of_three_sides):
    for opposite in range(1, sum_of_three_sides + 1):
        for adjacent in range(opposite + 1, sum_of_three_sides + 1):
            hypotenuse = sum_of_three_sides - opposite - adjacent
            if opposite * opposite + adjacent * adjacent == hypotenuse * hypotenuse:
                # It is now implied that adjacent < hypotenuse, because we have opposite > 0
                print(f"{opposite**2}, {adjacent**2}, {hypotenuse**2}")
                return opposite * adjacent * hypotenuse


if __name__ == "__main__":
    print(compute(1000))
    running_time.time_to_run()
