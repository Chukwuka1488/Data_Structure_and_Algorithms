"""
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example:
if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and
18 and the input will always be an integer.
"""

# def first_factorial(num):
#     value = 1
#     for i in range(1, num + 1):
#         value *= i
#
#     return value
#
#
# print(first_factorial(180000))


import decimal


def first_factorial(num):
    value = decimal.Decimal(1)
    for i in range(1, num + 1):
        value *= decimal.Decimal(i)

    return value


print(first_factorial(180000))
