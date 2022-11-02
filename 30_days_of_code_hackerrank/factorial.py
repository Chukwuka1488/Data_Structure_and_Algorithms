import os


def factorial(n):
    # Write your code here
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


if __name__ == '__main__':
    # OUTPUT_PATH = '/Volumes/Seagate_Haykay/All_Python/Coding_Practice_Tests/30_days_of_code_hackerrank'
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('factorial.txt', 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
