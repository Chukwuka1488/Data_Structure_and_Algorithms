# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
import math


def repeatedString(s, n):
    # Write your code here
    # empty string
    length = len(s)
    if length == 0 or (length == 1 and s != 'a'):
        return 0
    # 1 letter string
    if length == 1 and s == 'a':
        return n
    if length > 1:
        count_a = s.count('a')
        num = n // length
        mod = n % length
        remainder = s[:mod].count('a')

    return count_a * num + remainder


sen = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
print(repeatedString(sen, 736778906400))
