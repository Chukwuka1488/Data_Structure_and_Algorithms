def longest_alt_sub_array(arr):
    # If length of the array is 1
    # then return 1
    n = len(arr)

    if n == 1:
        return 1

    max_len = 0
    curr_largest = 0
    curr_smallest = 0

    # traverse the temp array
    for i in range(1, n):
        # If current element is greater
        # than the previous element
        if arr[i] > arr[i - 1]:
            # Increment currGreater by 1
            curr_largest += 1
            # Reset currSmaller to 0
            curr_smallest = 0
        # If current element is smaller
        # than the previous element
        elif arr[i] < arr[i - 1]:
            # Increment currSmaller by 1
            curr_largest = 0
            # Reset currGreater to 0
            curr_smallest += 1
        # If current element is equal
        # to previous element
        else:

            # Reset both to 0
            curr_largest = 0
            curr_smallest = 0
        # Swap currGreater and currSmaller
        # for the next iteration
        temp = curr_largest
        curr_largest = curr_smallest
        curr_smallest = temp
        # Update maxLen
        max_len = max(max_len, max(curr_largest, curr_smallest))
    return max_len + 1


print(longest_alt_sub_array([1, 2, 3, 2, 5, 7]))
