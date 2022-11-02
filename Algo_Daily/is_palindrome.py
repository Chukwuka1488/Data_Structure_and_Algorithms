def is_palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        # if the value at start idx is not alphanumeric and start is less than end, move start to next idx position
        while not s[start].isalnum() and start < end:
            start += 1
        # if the value at end idx is not alphanumeric and start is less than end, move start to backwards idx position
        while not s[end].isalnum() and start < end:
            end -= 1
        # if the start position idx values and end positions idx values are the same values,
        # move both start and end 1 step forward and 1 step backwards
        if s[start] == s[end] or s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("A Santa Lived As a Devil At NASA"))
