def longest_alt_sub_array(arr):

    n = len(arr)

    if n == 1:
        return 1

    max_len = 0
    curr_largest = 0
    curr_smallest = 0

    # traverse the temp array
    for i in range(1, n):

        if arr[i] > arr[i-1]:

            curr_largest += 1

            curr_smallest = 0
        
        elif arr[i] < arr[i-1]:

            curr_largest = 0

            curr_smallest += 0 

        else:
            
            curr_largest = 0
            curr_smallest = 0

        temp = curr_largest
        curr_largest = curr_smallest
        curr_smallest = temp

        max_len = max(max_len, max(curr_largest, curr_smallest))
    return max_len + 1

print(longest_alt_sub_array([1, 2, 3, 2, 5, 7]))

